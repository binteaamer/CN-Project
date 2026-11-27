import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/fairness_extended_results.csv")

df["algorithm_pair"] = (
    df["flow1_algorithm"] + " / " + df["flow2_algorithm"]
)

df["measurement_id"] = range(1, len(df) + 1)

summary = df.groupby(
    ["algorithm_pair", "rtt_condition"]
).agg(
    measurements=("measurement_id", "count"),
    avg_flow1=("flow1_throughput_mbps", "mean"),
    avg_flow2=("flow2_throughput_mbps", "mean"),
    avg_total=("total_throughput_mbps", "mean"),
    avg_fairness=("jains_fairness_index", "mean"),
    avg_flow1_retrans=("flow1_retransmissions", "mean"),
    avg_flow2_retrans=("flow2_retransmissions", "mean")
).round(4)

print("\n======================================")
print("EXTENDED TCP FAIRNESS ANALYSIS")
print("======================================")

print("\nAVERAGE RESULTS:\n")
print(summary.to_string())

summary.to_csv("results/fairness_extended_summary.csv")

df["experiment"] = (
    df["algorithm_pair"] + "\n" + df["rtt_condition"]
)

experiments = list(summary.index)

labels = [
    pair + "\n" + condition
    for pair, condition in experiments
]

# GRAPH 1: Jain's Fairness Index

plt.figure(figsize=(11, 6))

plt.bar(
    labels,
    [summary.loc[item, "avg_fairness"] for item in experiments]
)

plt.xlabel("Algorithm Pair and RTT Condition")
plt.ylabel("Jain's Fairness Index")
plt.title("Mixed TCP Algorithms: Fairness Comparison")
plt.ylim(0, 1.1)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/fairness_extended_jain.png")
plt.close()


# GRAPH 2: Individual Flow Throughput

plt.figure(figsize=(11, 6))

x = range(len(experiments))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    [summary.loc[item, "avg_flow1"] for item in experiments],
    width,
    label="Flow 1"
)

plt.bar(
    [i + width / 2 for i in x],
    [summary.loc[item, "avg_flow2"] for item in experiments],
    width,
    label="Flow 2"
)

plt.xlabel("Algorithm Pair and RTT Condition")
plt.ylabel("Throughput (Mbps)")
plt.title("Individual Flow Throughput: Mixed TCP Algorithms")
plt.xticks(list(x), labels)
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/fairness_extended_throughput.png")
plt.close()


# GRAPH 3: Total Throughput

plt.figure(figsize=(11, 6))

plt.bar(
    labels,
    [summary.loc[item, "avg_total"] for item in experiments]
)

plt.xlabel("Algorithm Pair and RTT Condition")
plt.ylabel("Total Throughput (Mbps)")
plt.title("Total Throughput: Mixed TCP Algorithms")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/fairness_extended_total.png")
plt.close()


# GRAPH 4: Retransmissions

plt.figure(figsize=(11, 6))

plt.bar(
    labels,
    [
        summary.loc[item, "avg_flow1_retrans"]
        + summary.loc[item, "avg_flow2_retrans"]
        for item in experiments
    ]
)

plt.xlabel("Algorithm Pair and RTT Condition")
plt.ylabel("Average Total Retransmissions")
plt.title("TCP Retransmissions: Mixed Algorithm Pairs")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/fairness_extended_retransmissions.png")
plt.close()


print("\nAll extended fairness graphs generated successfully!")
print("Saved in plots/ folder.")
print("Summary saved: results/fairness_extended_summary.csv")
