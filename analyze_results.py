import pandas as pd

df = pd.read_csv("results/tcp_matrix_results.csv")

summary = df.groupby(
    ["algorithm", "rtt_ms", "buffer_multiplier"]
).agg(
    avg_receiver_throughput=("receiver_throughput_mbps", "mean"),
    avg_sender_throughput=("sender_throughput_mbps", "mean"),
    avg_retransmissions=("retransmissions", "mean")
).reset_index()

summary = summary.round(3)

print("\n==========================================")
print("TCP CONGESTION CONTROL - RESULTS ANALYSIS")
print("==========================================")

print("\nAVERAGE RESULTS FOR EACH CONDITION:\n")
print(summary.to_string(index=False))

summary.to_csv("results/average_results.csv", index=False)

print("\nAnalysis completed successfully!")
print("Saved: results/average_results.csv")





What our results show so far
Algorithm	General observation
BBR	Consistently high receiver throughput, around 9 Mbps.
CUBIC	Strong throughput, particularly with larger buffers.
RENO	More retransmissions under some larger-buffer and higher-RTT conditions.


One important observation: Reno's sender throughput reaches 11.347 Mbps despite the configured 10 Mbps bottleneck. We'll treat receiver throughput as our primary goodput measurement and investigate sender-side discrepancies before drawing conclusions.
run to see graphs : python -c "import pandas, matplotlib; print('Both libraries are ready!')"






