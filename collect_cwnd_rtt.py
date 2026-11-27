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
SAMPLE_INTERVAL = 0.05

ALGORITHMS = ["reno", "cubic", "bbr"]

OUTPUT_FILE = "results/cwnd_rtt_timeseries_updated.csv"


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

                connections = re.split(r"(?=ESTAB)", result)

                data_connection = None
                largest_bytes = -1

                for connection in connections:

                    bytes_match = re.search(
                        r"bytes_sent:(\d+)", connection
                    )

                    if bytes_match:

                        sent_bytes = int(bytes_match.group(1))

                        if sent_bytes > largest_bytes:
                            largest_bytes = sent_bytes
                            data_connection = connection

                if data_connection:

                    cwnd_match = re.search(
                        r"cwnd:(\d+)", data_connection
                    )

                    ssthresh_match = re.search(
                        r"ssthresh:(\d+)", data_connection
                    )

                    rtt_match = re.search(
                        r"rtt:([\d.]+)", data_connection
                    )

                    retrans_match = re.search(
                        r"retrans:(\d+)/(\d+)", data_connection
                    )

                    if cwnd_match and rtt_match:

                        elapsed = time.monotonic() - start_time

                        retransmissions = 0

                        if retrans_match:
                            retransmissions = int(
                                retrans_match.group(1)
                            )

                        ssthresh = ""

                        if ssthresh_match:
                            ssthresh = int(
                                ssthresh_match.group(1)
                            )

                        samples.append({
                            "timestamp": datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S.%f"
                            ),
                            "algorithm": algorithm.upper(),
                            "time_seconds": round(elapsed, 3),
                            "cwnd_segments": int(cwnd_match.group(1)),
                            "ssthresh_segments": ssthresh,
                            "rtt_ms": round(
                                float(rtt_match.group(1)), 3
                            ),
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
                    "ssthresh_segments",
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
