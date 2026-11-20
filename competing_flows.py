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

ALGORITHMS = ["reno", "cubic", "bbr"]

RTT_MS = 100
BUFFER_MULTIPLIER = 1

TEST_DURATION = 30
REPETITIONS = 3

SERVER1_IP = "10.0.4.2"
SERVER2_IP = "10.0.5.2"

SERVER1_PORT = 5201
SERVER2_PORT = 5202

RESULT_FOLDER = "results"
CSV_FILE = os.path.join(RESULT_FOLDER, "fairness_results.csv")


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

def run_competing_test(algorithm, repetition):

    print("\n======================================")
    print("Algorithm:", algorithm.upper())
    print("Repetition:", repetition)
    print("======================================")

    queue_size = calculate_queue_size(
        RTT_MS,
        BUFFER_MULTIPLIER
    )

    net = start_network(RTT_MS, queue_size)

    try:

        h1 = net.get("h1")
        h2 = net.get("h2")
        h3 = net.get("h3")
        h4 = net.get("h4")

        # Configure congestion control on both senders
        h1.cmd(
            "sysctl -w net.ipv4.tcp_congestion_control=" + algorithm
        )

        h2.cmd(
            "sysctl -w net.ipv4.tcp_congestion_control=" + algorithm
        )

        # Start iperf3 server on Host 3
        h3.cmd("iperf3 -s -p 5201 -D")

        # Start iperf3 server on Host 4
        h4.cmd("iperf3 -s -p 5202 -D")

        time.sleep(2)

        print("Starting both TCP flows simultaneously...")

        # Flow 1: h1 -> h3
        flow1 = h1.popen(
            "iperf3 -c 10.0.4.2 -p 5201 -t "
            + str(TEST_DURATION) + " -J",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Flow 2: h2 -> h4
        flow2 = h2.popen(
            "iperf3 -c 10.0.5.2 -p 5202 -t "
            + str(TEST_DURATION) + " -J",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Wait for both flows to finish
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
            data1["end"]["sum_received"]["bits_per_second"] / 1000000
        )

        throughput2 = (
            data2["end"]["sum_received"]["bits_per_second"] / 1000000
        )

        # Extract sender retransmissions
        retrans1 = data1["end"]["sum_sent"].get("retransmits", 0)
        retrans2 = data2["end"]["sum_sent"].get("retransmits", 0)

        # Calculate total throughput and fairness
        total_throughput = throughput1 + throughput2

        fairness = calculate_fairness(
            throughput1,
            throughput2
        )

        print("\nExperiment Results:")
        print("Flow 1 Throughput:", round(throughput1, 3), "Mbps")
        print("Flow 2 Throughput:", round(throughput2, 3), "Mbps")
        print("Total Throughput:", round(total_throughput, 3), "Mbps")
        print("Flow 1 Retransmissions:", retrans1)
        print("Flow 2 Retransmissions:", retrans2)
        print("Jain's Fairness Index:", round(fairness, 4))

        # Prepare CSV result
        result = {
            "algorithm": algorithm.upper(),
            "repetition": repetition,
            "rtt_ms": RTT_MS,
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
        h3.cmd("pkill -x iperf3")
        h4.cmd("pkill -x iperf3")

        # Stop Mininet network
        net.stop()


# ============================================================
# SECTION 4: SAVE RESULTS TO CSV
# ============================================================

def save_result(result):

    os.makedirs(RESULT_FOLDER, exist_ok=True)

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=result.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)


# ============================================================
# SECTION 5: MAIN EXPERIMENT
# ============================================================

def main():

    setLogLevel("warning")

    print("\n======================================")
    print("TCP COMPETING FLOWS FAIRNESS EXPERIMENT")
    print("======================================")

    print("Algorithms:", ALGORITHMS)
    print("RTT:", RTT_MS, "ms")
    print("Buffer multiplier:", BUFFER_MULTIPLIER)
    print("Test duration:", TEST_DURATION, "seconds")
    print("Repetitions:", REPETITIONS)

    for algorithm in ALGORITHMS:

        for repetition in range(1, REPETITIONS + 1):

            result = run_competing_test(
                algorithm,
                repetition
            )

            save_result(result)

    print("\n======================================")
    print("ALL FAIRNESS EXPERIMENTS COMPLETED")
    print("======================================")

    print("Results saved to:", CSV_FILE)


if __name__ == "__main__":

main()






python -m py_compile measurement/competing_flows.py
