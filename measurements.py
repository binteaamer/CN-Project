
# ============================================================
# SECTION 1: IMPORT LIBRARIES
# ============================================================

import csv
import json
import os
import time
import subprocess
from datetime import datetime


# ============================================================
# SECTION 2: EXPERIMENT SETTINGS
# ============================================================

# TCP congestion control algorithms to compare
ALGORITHMS = ["reno", "cubic", "bbr"]

# Duration of each test in seconds
TEST_DURATION = 30

# Bottleneck server address (Host 3)
SERVER_IP = "10.0.4.2"

# iPerf3 server port
SERVER_PORT = 5201

# Number of repetitions for each algorithm
REPETITIONS = 3

# Location where results will be stored
RESULT_FOLDER = "results"

# CSV output file
CSV_FILE = os.path.join(RESULT_FOLDER, "tcp_results.csv")


# ============================================================
# SECTION 3: CREATE RESULTS FOLDER
# ============================================================

os.makedirs(RESULT_FOLDER, exist_ok=True)


# ============================================================
# SECTION 4: CHECK REQUIRED COMMANDS
# ============================================================

def check_command(command):

    result = subprocess.run(
        ["which", command],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(command + " is not installed.")


# ============================================================
# SECTION 5: START IPERF3 SERVER
# ============================================================

def start_server():

    # Start iPerf3 server on Host 3
    command = [
        "iperf3",
        "-s",
        "-p",
        str(SERVER_PORT),
        "-1"
    ]

    server = subprocess.Popen(
        ["mnexec", "-a", get_host_pid("h3")] + command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(2)

    return server


# ============================================================
# SECTION 6: GET MININET HOST PROCESS ID
# ============================================================

def get_host_pid(host):

    result = subprocess.run(
        ["pgrep", "-f", "mininet:" + host],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError("Could not find Mininet host " + host)

    return result.stdout.strip().split("\n")[0]


# ============================================================
# SECTION 7: RUN ONE TCP EXPERIMENT
# ============================================================

def run_test(algorithm, repetition):

    print("\nRunning:", algorithm.upper())
    print("Repetition:", repetition)

    # Start the iPerf3 server
    server = start_server()

    # Select the congestion control algorithm on Host 1
    subprocess.run(
        [
            "mnexec",
            "-a",
            get_host_pid("h1"),
            "sysctl",
            "-w",
            "net.ipv4.tcp_congestion_control=" + algorithm
        ],
        check=True,
        capture_output=True,
        text=True
    )

    # Give the server time to start
    time.sleep(2)

    # Run iPerf3 client on Host 1
    command = [
        "mnexec",
        "-a",
        get_host_pid("h1"),
        "iperf3",
        "-c",
        SERVER_IP,
        "-p",
        str(SERVER_PORT),
        "-t",
        str(TEST_DURATION),
        "-J"
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        server.terminate()
        raise RuntimeError(result.stderr)

    # Convert JSON output into Python data
    data = json.loads(result.stdout)

    # Extract sender measurements
    sender = data["end"]["sum_sent"]

    # Extract receiver measurements
    receiver = data["end"]["sum_received"]

    # Prepare one row of results
    row = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "algorithm": algorithm.upper(),
        "repetition": repetition,
        "duration_seconds": TEST_DURATION,
        "sender_throughput_mbps": round(
            sender["bits_per_second"] / 1000000, 3
        ),
        "receiver_throughput_mbps": round(
            receiver["bits_per_second"] / 1000000, 3
        ),
        "retransmissions": sender.get("retransmits", 0)
    }

    # Stop the server process
    server.terminate()
    server.wait(timeout=5)

    return row


# ============================================================
# SECTION 8: SAVE RESULTS TO CSV
# ============================================================

def save_result(row):

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:

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

    # Check that required programs are installed
    check_command("iperf3")
    check_command("mnexec")

    print("\n===================================")
    print(" TCP CONGESTION CONTROL EXPERIMENT")
    print("===================================")

    print("Algorithms:", ALGORITHMS)
    print("Duration:", TEST_DURATION, "seconds")
    print("Repetitions:", REPETITIONS)

    # Run each algorithm multiple times
    for algorithm in ALGORITHMS:

        for repetition in range(1, REPETITIONS + 1):

            row = run_test(algorithm, repetition)

            save_result(row)

            print("\nResult:")
            print(row)

            # Small gap between experiments
            time.sleep(3)

    print("\n===================================")
    print(" ALL EXPERIMENTS COMPLETED")
    print("===================================")

    print("Results saved in:", CSV_FILE)


# ============================================================
# SECTION 10: PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()
