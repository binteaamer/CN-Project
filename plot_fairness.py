import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/fairness_results.csv")

algorithms = ["RENO", "CUBIC", "BBR"]

summary = df.groupby("algorithm").agg(
    avg_flow1=("flow1_throughput_mbps", "mean"),
    avg_flow2=("flow2_throughput_mbps", "mean"),
    avg_total=("total_throughput_mbps", "mean"),
    avg_fairness=("jains_fairness_index", "mean")
).reindex(algorithms).round(4)

print("\n======================================")
print("TCP COMPETING FLOWS - FAIRNESS ANALYSIS")
print("======================================")

print("\nAVERAGE RESULTS:\n")
print(summary.to_string())

# GRAPH 1: Jain's Fairness Index

plt.figure(figsize=(9, 6))

plt.bar(
    algorithms,
    summary["avg_fairness"]
)

plt.xlabel("TCP Algorithm")
plt.ylabel("Jain's Fairness Index")
plt.title("TCP Algorithms: Fairness Comparison")
plt.ylim(0, 1.1)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/fairness_comparison.png")
plt.close()


# GRAPH 2: Individual Flow Throughput

plt.figure(figsize=(9, 6))

x = range(len(algorithms))
width = 0.35

plt.bar(
    [i - width / 2 for i in x],
    summary["avg_flow1"],
    width,
    label="Flow 1 (h1 to h3)"
)

plt.bar(
    [i + width / 2 for i in x],
    summary["avg_flow2"],
    width,
    label="Flow 2 (h2 to h4)"
)

plt.xlabel("TCP Algorithm")
plt.ylabel("Receiver Throughput (Mbps)")
plt.title("Individual Flow Throughput Comparison")
plt.xticks(list(x), algorithms)
plt.legend()
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/individual_flow_throughput.png")
plt.close()


# GRAPH 3: Total Throughput

plt.figure(figsize=(9, 6))

plt.bar(
    algorithms,
    summary["avg_total"]
)

plt.xlabel("TCP Algorithm")
plt.ylabel("Total Throughput (Mbps)")
plt.title("Total Throughput Under Competing Flows")
plt.ylim(0, 10.5)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("plots/total_throughput_fairness.png")
plt.close()


# SAVE SUMMARY

summary.to_csv("results/fairness_summary.csv")

print("\nAll fairness graphs generated successfully!")
print("Saved in plots/ folder.")
print("Summary saved: results/fairness_summary.csv")
