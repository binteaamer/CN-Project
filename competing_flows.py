import csv
import json
import os
import time
import subprocess

from mininet.log import setLogLevel
from measurement.run_experiment import start_network, calculate_queue_size


# ============================================================
# SECTION 1: EXPERIMENT CONFIGURATION
# ============================================================

MIXED_PAIRS = [
    ("reno", "cubic"),
    ("reno", "bbr"),
    ("cubic", "bbr")
]

RTT_MS = 100
BUFFER_MULTIPLIER = 1

EXTRA_DELAY_MS = 25

TEST_DURATION = 30
REPETITIONS = 3

SERVER1_IP = "10.0.3.10"
SERVER2_IP = "10.0.3.11"

SERVER1_PORT = 5201
SERVER2_PORT = 5202

RESULT_FOLDER = "results"

CSV_FILE = os.path.join(
    RESULT_FOLDER,
    "fairness_results.csv"
)

EXTENDED_CSV_FILE = os.path.join(
    RESULT_FOLDER,
    "fairness_extended_results.csv"
)


# ============================================================
# SECTION 2: CALCULATE JAIN'S FAIRNESS INDEX
# ============================================================

def calculate_fairness(x1, x2):

    numerator = (x1 + x2) ** 2
    denominator = 2 * (x1 ** 2 + x2 ** 2)

    if denominator == 0:
        return 0

    return numerator / denominator


# ============================================================
# SECTION 3: RUN TWO COMPETING TCP FLOWS
# ============================================================

def run_competing_test(
    algorithm1,
    algorithm2,
    repetition,
    unequal_rtt
):

    print("\n======================================")
    print("Flow 1 Algorithm:", algorithm1.upper())
    print("Flow 2 Algorithm:", algorithm2.upper())
    print("Repetition:", repetition)

    if unequal_rtt:
        print("RTT Condition: UNEQUAL")
    else:
        print("RTT Condition: EQUAL")

    print("======================================")

    queue_size = calculate_queue_size(
        RTT_MS,
        BUFFER_MULTIPLIER
    )

    net = start_network(RTT_MS, queue_size)

    h1 = None
    h2 = None
    h3 = None
    h4 = None

    try:

        h1 = net.get("h1")
        h2 = net.get("h2")
        h3 = net.get("h3")
        h4 = net.get("h4")

        # Configure congestion control algorithms

        h1.cmd(
            "sysctl -w net.ipv4.tcp_congestion_control="
            + algorithm1
        )

        h2.cmd(
            "sysctl -w net.ipv4.tcp_congestion_control="
            + algorithm2
        )

        # Apply additional delay to Flow 2

        if unequal_rtt:

            h2.cmd(
                "tc qdisc add dev h2-eth0 root netem delay "
                + str(EXTRA_DELAY_MS) + "ms"
            )

            h4.cmd(
                "tc qdisc add dev h4-eth0 root netem delay "
                + str(EXTRA_DELAY_MS) + "ms"
            )

        # Start iperf3 servers

        h3.cmd(
            "iperf3 -s -p "
            + str(SERVER1_PORT) + " -D"
        )

        h4.cmd(
            "iperf3 -s -p "
            + str(SERVER2_PORT) + " -D"
        )

        time.sleep(2)

        print("\nStarting both TCP flows simultaneously...")

        # Flow 1: h1 -> h3

        flow1 = h1.popen(
            "iperf3 -c " + SERVER1_IP
            + " -p " + str(SERVER1_PORT)
            + " -t " + str(TEST_DURATION)
            + " -J",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Flow 2: h2 -> h4

        flow2 = h2.popen(
            "iperf3 -c " + SERVER2_IP
            + " -p " + str(SERVER2_PORT)
            + " -t " + str(TEST_DURATION)
            + " -J",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Wait for both flows

        output1, error1 = flow1.communicate()
        output2, error2 = flow2.communicate()

        if flow1.returncode != 0:
            raise RuntimeError("Flow 1 failed: " + error1)

        if flow2.returncode != 0:
            raise RuntimeError("Flow 2 failed: " + error2)

        # Parse iperf3 JSON results

        data1 = json.loads(output1)
        data2 = json.loads(output2)

        # Extract receiver throughput

        throughput1 = (
            data1["end"]["sum_received"]["bits_per_second"]
            / 1000000
        )

        throughput2 = (
            data2["end"]["sum_received"]["bits_per_second"]
            / 1000000
        )

        # Extract sender retransmissions

        retrans1 = data1["end"]["sum_sent"].get(
            "retransmits", 0
        )

        retrans2 = data2["end"]["sum_sent"].get(
            "retransmits", 0
        )

        # Calculate total throughput and fairness

        total_throughput = throughput1 + throughput2

        fairness = calculate_fairness(
            throughput1,
            throughput2
        )

        print("\nExperiment Results:")

        print(
            "Flow 1 Throughput:",
            round(throughput1, 3),
            "Mbps"
        )

        print(
            "Flow 2 Throughput:",
            round(throughput2, 3),
            "Mbps"
        )

        print(
            "Total Throughput:",
            round(total_throughput, 3),
            "Mbps"
        )

        print("Flow 1 Retransmissions:", retrans1)
        print("Flow 2 Retransmissions:", retrans2)

        print(
            "Jain's Fairness Index:",
            round(fairness, 4)
        )

        # Prepare extended CSV result

        result = {
            "flow1_algorithm": algorithm1.upper(),
            "flow2_algorithm": algorithm2.upper(),
            "rtt_condition": (
                "UNEQUAL" if unequal_rtt else "EQUAL"
            ),
            "base_rtt_ms": RTT_MS,
            "flow1_extra_delay_ms": 0,
            "flow2_extra_delay_ms": (
                EXTRA_DELAY_MS if unequal_rtt else 0
            ),
            "repetition": repetition,
            "buffer_multiplier": BUFFER_MULTIPLIER,
            "queue_size": queue_size,
            "flow1_throughput_mbps": round(throughput1, 3),
            "flow2_throughput_mbps": round(throughput2, 3),
            "total_throughput_mbps": round(total_throughput, 3),
            "flow1_retransmissions": retrans1,
            "flow2_retransmissions": retrans2,
            "jains_fairness_index": round(fairness, 4)
        }

        return result

    finally:

        # Stop iperf3 servers

        if h3 is not None:
            h3.cmd("pkill -x iperf3")

        if h4 is not None:
            h4.cmd("pkill -x iperf3")

        # Stop Mininet network

        net.stop()


# ============================================================
# SECTION 4: SAVE EXTENDED RESULTS TO CSV
# ============================================================

def save_result(result):

    os.makedirs(RESULT_FOLDER, exist_ok=True)

    file_exists = os.path.isfile(EXTENDED_CSV_FILE)

    with open(EXTENDED_CSV_FILE, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=result.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)


# ============================================================
# SECTION 5: MAIN EXTENDED EXPERIMENT
# ============================================================

def main():

    setLogLevel("warning")

    print("\n======================================")
    print("EXTENDED TCP FAIRNESS EXPERIMENT")
    print("======================================")

    print("Mixed algorithm pairs:", MIXED_PAIRS)
    print("Base RTT:", RTT_MS, "ms")
    print("Extra delay:", EXTRA_DELAY_MS, "ms")
    print("Buffer multiplier:", BUFFER_MULTIPLIER)
    print("Test duration:", TEST_DURATION, "seconds")
    print("Repetitions:", REPETITIONS)

    for algorithm1, algorithm2 in MIXED_PAIRS:

        for unequal_rtt in [False, True]:

            for repetition in range(1, REPETITIONS + 1):

                result = run_competing_test(
                    algorithm1,
                    algorithm2,
                    repetition,
                    unequal_rtt
                )

                save_result(result)

    print("\n======================================")
    print("ALL EXTENDED FAIRNESS EXPERIMENTS COMPLETED")
    print("======================================")

    print(
        "Results saved to:",
        EXTENDED_CSV_FILE
    )


if __name__ == "__main__":
    main()
