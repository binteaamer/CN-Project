import csv
import os
import re
import time
from datetime import datetime

from mininet.log import setLogLevel
from measurement.run_experiment import (
    start_network,
    start_server,
    SERVER_IP,
    SERVER_PORT
)

RTT_MS = 100
QUEUE_SIZE = 83
DURATION = 30
SAMPLE_INTERVAL = 0.2

ALGORITHMS = ["reno", "cubic", "bbr"]

OUTPUT_FILE = "results/cwnd_rtt_timeseries.csv"


def collect_measurements(h1, algorithm):

    print("\nStarting", algorithm.upper())

    h1.cmd(
        "sysctl -w net.ipv4.tcp_congestion_control=" + algorithm
    )

    samples = []

    command = [
        "iperf3",
        "-c", SERVER_IP,
        "-p", str(SERVER_PORT),
        "-t", str(DURATION)
    ]

    with open("/tmp/cwnd_iperf_output.txt", "w") as output_file:
        with open("/tmp/cwnd_iperf_error.txt", "w") as error_file:

            process = h1.popen(
                command,
                stdout=output_file,
                stderr=error_file
            )

            start_time = time.monotonic()

            while process.poll() is None:

                result = h1.cmd("ss -tin dst " + SERVER_IP)

                cwnd_match = re.search(r"cwnd:(\d+)", result)
                rtt_match = re.search(r"rtt:([\d.]+)", result)
                retrans_match = re.search(r"retrans:(\d+)/(\d+)", result)

                if cwnd_match and rtt_match:

                    elapsed = time.monotonic() - start_time

                    retransmissions = 0

                    if retrans_match:
                        retransmissions = int(retrans_match.group(1))

                    samples.append({
                        "timestamp": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S.%f"
                        ),
                        "algorithm": algorithm.upper(),
                        "time_seconds": round(elapsed, 3),
                        "cwnd_segments": int(cwnd_match.group(1)),
                        "rtt_ms": round(float(rtt_match.group(1)), 3),
                        "retransmissions": retransmissions
                    })

                time.sleep(SAMPLE_INTERVAL)

            process.wait()

    print("Samples collected:", len(samples))

    return samples


def main():

    os.makedirs("results", exist_ok=True)

    setLogLevel("warning")

    net = None
    all_samples = []

    try:

        net = start_network(RTT_MS, QUEUE_SIZE)

        h1 = net.get("h1")
        h3 = net.get("h3")

        if net.ping([h1, h3]) != 0:
            raise RuntimeError("Network connectivity failed.")

        start_server(h3)

        for algorithm in ALGORITHMS:

            samples = collect_measurements(h1, algorithm)

            all_samples.extend(samples)

            time.sleep(2)

    finally:

        if net is not None:
            net.stop()

    if all_samples:

        with open(OUTPUT_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "timestamp",
                    "algorithm",
                    "time_seconds",
                    "cwnd_segments",
                    "rtt_ms",
                    "retransmissions"
                ]
            )

            writer.writeheader()
            writer.writerows(all_samples)

        print("\nMeasurements saved successfully.")
        print("File:", OUTPUT_FILE)
        print("Total samples:", len(all_samples))

    else:

        print("No measurements were collected.")


if __name__ == "__main__":
    main()
