import csv
import os
import matplotlib.pyplot as plt

INPUT_FILE = "results/cwnd_rtt_timeseries_50ms.csv"
SSTHRESH_LIMIT = 300

os.makedirs("plots", exist_ok=True)

data = {}

with open(INPUT_FILE, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        algorithm = row["algorithm"]

        if algorithm not in data:
            data[algorithm] = {
                "time": [],
                "cwnd": [],
                "ssthresh": [],
                "rtt": []
            }

        data[algorithm]["time"].append(float(row["time_seconds"]))
        data[algorithm]["cwnd"].append(int(row["cwnd_segments"]))
        data[algorithm]["ssthresh"].append(int(row["ssthresh_segments"]))
        data[algorithm]["rtt"].append(float(row["rtt_ms"]))

algorithms = ["RENO", "CUBIC", "BBR"]

for algorithm in algorithms:
    if algorithm not in data:
        raise ValueError("Missing measurements for " + algorithm)

# GRAPH 1: CWND VS TIME

plt.figure(figsize=(12, 6))

for algorithm in algorithms:
    plt.plot(
        data[algorithm]["time"],
        data[algorithm]["cwnd"],
        label=algorithm,
        linewidth=1.2
    )

plt.title("TCP Congestion Window vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Congestion Window (segments)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plots/cwnd_vs_time.png", dpi=300)
plt.close()

# GRAPH 2: RTT VS TIME

plt.figure(figsize=(12, 6))

for algorithm in algorithms:
    plt.plot(
        data[algorithm]["time"],
        data[algorithm]["rtt"],
        label=algorithm,
        linewidth=1.2
    )

plt.title("TCP Round Trip Time vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Round Trip Time (ms)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plots/rtt_vs_time.png", dpi=300)
plt.close()

# GRAPH 3: SSTHRESH VS TIME

outlier_count = 0
outlier_values = set()

plt.figure(figsize=(12, 6))

for algorithm in algorithms:

    time_values = data[algorithm]["time"]
    ssthresh_values = data[algorithm]["ssthresh"]

    plotted_values = []

    for value in ssthresh_values:
        if value > SSTHRESH_LIMIT:
            outlier_count += 1
            outlier_values.add(value)
            plotted_values.append(float("nan"))
        else:
            plotted_values.append(value)

    plt.plot(
        time_values,
        plotted_values,
        label=algorithm,
        linewidth=1.5
    )

plt.title("TCP Slow Start Threshold vs Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Slow Start Threshold (segments)")

plt.ylim(0, SSTHRESH_LIMIT)

if outlier_count > 0:
    outlier_text = (
        str(outlier_count)
        + " observations above "
        + str(SSTHRESH_LIMIT)
        + " segments omitted from plotted lines; retained in CSV."
    )

    plt.text(
        0.02,
        0.96,
        outlier_text,
        transform=plt.gca().transAxes,
        va="top",
        fontsize=9
    )

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("plots/ssthresh_vs_time.png", dpi=300)
plt.close()

# DISPLAY RESULTS

print("\nGraphs generated successfully!")

print("\nSaved graphs:")
print("1. plots/cwnd_vs_time.png")
print("2. plots/rtt_vs_time.png")
print("3. plots/ssthresh_vs_time.png")

print("\nSSTHRESH outlier information:")
print("Observations above", SSTHRESH_LIMIT, "segments:", outlier_count)

if outlier_values:
    print("Unusual values:", sorted(outlier_values))

print("\nThese observations were omitted from the SSTHRESH plot only.")
print("Original CSV data has not been modified.")
