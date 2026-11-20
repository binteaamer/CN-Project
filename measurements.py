It includes:
- Reno, CUBIC and BBR.
- RTT values of 20, 50 and 100 ms.
- Buffer sizes of 0.5×, 1× and 2× BDP.
- Automatic BDP and queue-size calculation.
- Three repetitions per configuration.
- Automatic Mininet network creation and cleanup.
- CSV result storage.
- Progress tracking.


```python
# ============================================================
# TCP CONGESTION CONTROL EXPERIMENT
# Reno vs CUBIC vs BBR
# ============================================================


# ============================================================
# SECTION 1: IMPORT LIBRARIES
# ============================================================

import csv
import json
import os
import time
import subprocess
from datetime import datetime

from mininet.log import setLogLevel

from topology.dumbbell import (
    DumbbellTopo,
    configure_network,
    configure_routers,
    configure_routes
)

from mininet.net import Mininet
from mininet.link import TCLink


# ============================================================
# SECTION 2: EXPERIMENT CONFIGURATION
# ============================================================

ALGORITHMS = ["reno", "cubic", "bbr"]

TEST_DURATION = 30
REPETITIONS = 3

SERVER_IP = "10.0.4.2"
SERVER_PORT = 5201

BOTTLENECK_BW = 10

RTT_VALUES = [20, 50, 100]

BUFFER_MULTIPLIERS = [0.5, 1, 2]

PACKET_SIZE_BYTES = 1500

RESULT_FOLDER = "results"

CSV_FILE = os.path.join(
    RESULT_FOLDER,
    "tcp_matrix_results.csv"
)


# ============================================================
# SECTION 3: CREATE RESULTS FOLDER
# ============================================================

os.makedirs(RESULT_FOLDER, exist_ok=True)


# ============================================================
# SECTION 4: START MININET NETWORK
# ============================================================

def start_network(rtt_ms, queue_size):

    print("\nStarting Mininet topology...")

    print("Target RTT:", rtt_ms, "ms")

    print("Queue size:", queue_size, "packets")

    one_way_delay = str(rtt_ms // 2) + "ms"

    topo = DumbbellTopo(
        bw=BOTTLENECK_BW,
        delay=one_way_delay,
        max_queue_size=queue_size
    )

    net = Mininet(
        topo=topo,
        link=TCLink,
        controller=None,
        autoSetMacs=True
    )

    net.start()

    configure_network(net)

    configure_routers(net)

    configure_routes(net)

    print("Network started successfully.")

    return net


# ============================================================
# SECTION 5: BDP AND BUFFER SIZE CALCULATION
# ============================================================

def calculate_queue_size(rtt_ms, multiplier):

    bandwidth_bps = BOTTLENECK_BW * 1000000

    rtt_seconds = rtt_ms / 1000

    bdp_bytes = (
        bandwidth_bps * rtt_seconds
    ) / 8

    bdp_packets = (
        bdp_bytes / PACKET_SIZE_BYTES
    )

    queue_size = round(
        bdp_packets * multiplier
    )

    return max(1, queue_size)


# ============================================================
# SECTION 6: START IPERF3 SERVER
# ============================================================

def start_server(h3):

    server = h3.popen(
        [
            "iperf3",
            "-s",
            "-p",
            str(SERVER_PORT),
            "-1"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True
    )

    time.sleep(2)

    return server


# ============================================================
# SECTION 7: RUN ONE TCP EXPERIMENT
# ============================================================

def run_test(
    net,
    algorithm,
    repetition,
    rtt_ms,
    buffer_multiplier,
    queue_size
):

    print("\n-----------------------------------")

    print("Algorithm:", algorithm.upper())

    print("Repetition:", repetition)

    print("RTT:", rtt_ms, "ms")

    print("Buffer:", buffer_multiplier, "x BDP")

    print("Queue size:", queue_size, "packets")

    print("-----------------------------------")

    h1 = net.get("h1")

    h3 = net.get("h3")

    # Select TCP congestion control algorithm

    h1.cmd(
        "sysctl -w net.ipv4.tcp_congestion_control="
        + algorithm
    )

    # Start one-time iPerf3 server

    server = start_server(h3)

    try:

        # Run iPerf3 client

        command = (
            "iperf3 -c " + SERVER_IP
            + " -p " + str(SERVER_PORT)
            + " -t " + str(TEST_DURATION)
            + " -J"
        )

        output = h1.cmd(command)

        # Convert JSON output into Python data

        data = json.loads(output)

        # Extract sender measurements

        sender = data["end"]["sum_sent"]

        # Extract receiver measurements

        receiver = data["end"]["sum_received"]

        # Prepare experiment results

        row = {

            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "algorithm": algorithm.upper(),

            "repetition": repetition,

            "duration_seconds": TEST_DURATION,

            "bandwidth_mbps": BOTTLENECK_BW,

            "rtt_ms": rtt_ms,

            "buffer_multiplier": buffer_multiplier,

            "queue_size": queue_size,

            "sender_throughput_mbps": round(
                sender["bits_per_second"] / 1000000,
                3
            ),

            "receiver_throughput_mbps": round(
                receiver["bits_per_second"] / 1000000,
                3
            ),

            "retransmissions": sender.get(
                "retransmits",
                0
            )
        }

        return row

    finally:

        # Ensure the one-time server process is cleaned up

        if server.poll() is None:

            server.terminate()

            try:

                server.wait(timeout=3)

            except subprocess.TimeoutExpired:

                server.kill()

                server.wait()


# ============================================================
# SECTION 8: SAVE RESULTS TO CSV
# ============================================================

def save_result(row):

    file_exists = os.path.exists(CSV_FILE)

    with open(
        CSV_FILE,
        "a",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=row.keys()
        )

        if not file_exists:

            writer.writeheader()

        writer.writerow(row)


# ============================================================
# SECTION 9: RUN ALL EXPERIMENTS
# ============================================================

def main():

    print("\n===================================")

    print("TCP CONGESTION CONTROL EXPERIMENT")

    print("===================================")

    print("Algorithms:", ALGORITHMS)

    print("RTT values:", RTT_VALUES)

    print("Buffer multipliers:", BUFFER_MULTIPLIERS)

    print("Test duration:", TEST_DURATION)

    print("Repetitions:", REPETITIONS)

    setLogLevel("warning")

    total_experiments = (

        len(ALGORITHMS)

        * len(RTT_VALUES)

        * len(BUFFER_MULTIPLIERS)

        * REPETITIONS

    )

    completed = 0

    try:

        for rtt_ms in RTT_VALUES:

            for buffer_multiplier in BUFFER_MULTIPLIERS:

                queue_size = calculate_queue_size(
                    rtt_ms,
                    buffer_multiplier
                )

                print("\n===================================")

                print("NEW NETWORK CONFIGURATION")

                print("RTT:", rtt_ms, "ms")

                print(
                    "Buffer:",
                    buffer_multiplier,
                    "x BDP"
                )

                print(
                    "Queue:",
                    queue_size,
                    "packets"
                )

                print("===================================")

                net = None

                try:

                    # Start network with current configuration

                    net = start_network(
                        rtt_ms,
                        queue_size
                    )

                    # Check network connectivity

                    if net.ping(
                        [
                            net.get("h1"),
                            net.get("h3")
                        ]
                    ) != 0:

                        raise RuntimeError(
                            "Network connectivity failed."
                        )

                    # Run all TCP algorithms

                    for algorithm in ALGORITHMS:

                        for repetition in range(
                            1,
                            REPETITIONS + 1
                        ):

                            row = run_test(
                                net,
                                algorithm,
                                repetition,
                                rtt_ms,
                                buffer_multiplier,
                                queue_size
                            )

                            save_result(row)

                            completed += 1

                            print("\nExperiment result:")

                            print(row)

                            print(
                                "Progress:",
                                completed,
                                "/",
                                total_experiments
                            )

                            time.sleep(3)

                finally:

                    if net is not None:

                        print(
                            "\nStopping Mininet network..."
                        )

                        net.stop()

        print("\n===================================")

        print("ALL EXPERIMENTS COMPLETED")

        print("===================================")

    except Exception as error:

        print("\nExperiment failed:", error)

        raise

    print(
        "Completed:",
        completed,
        "/",
        total_experiments
    )

    print("CSV file:", CSV_FILE)


# ============================================================
# SECTION 10: PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
```





// measurements 
running commands on ubuntu:   sudo python3 -m measurement.run_experimenty
run :python3 -c "from measurement.run_experiment import calculate_queue_size;
[(print(rtt, [calculate_queue_size(rtt, m) for m in [0.5, 1, 2]])) for rtt in [20, 50, 100]]"


results :

1. What your results show
Your experiment used:
- Bottleneck bandwidth: 10 Mbps
- Approximate RTT: 20 ms (10 ms in each direction)
- Queue size: 100 packets
- Test duration: 30 seconds
- Repetitions: 3 per algorithm
Here are the average results:
Algorithm	Avg. Receiver Throughput	Avg. Retransmissions
Reno	9.167 Mbps	436
CUBIC	9.128 Mbps	25.3
BBR	9.139 Mbps	0


Initial interpretation
- Reno: Achieved slightly higher average receiver throughput, but experienced considerably more retransmissions.
- CUBIC: Delivered similar throughput with substantially fewer retransmissions.
- BBR: Delivered similar throughput with zero reported retransmissions in all three trials.
These are preliminary observations, not final conclusions. We still need to test different RTTs and buffer sizes before comparing the algorithms properly.






SETTINGS 
Setting	Verified value
Test duration	30 seconds
Repetitions	3
RTT values	20, 50, 100 ms
Buffer multipliers	0.5, 1, 2


Final experiment: 81 runs
The calculation is:

3 RTTs × 3 buffer sizes × 3 algorithms × 3 repetitions = 81 experiments.
                                                      
