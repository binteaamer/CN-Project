import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/average_results.csv")

algorithms = ["RENO", "CUBIC", "BBR"]
rtts = [20, 50, 100]
buffers = [0.5, 1.0, 2.0]

# GRAPH 1: Average Receiver Throughput

plt.figure(figsize=(10, 6))

for algorithm in algorithms:
    data = df[df["algorithm"] == algorithm]
    averages = data.groupby("rtt_ms")["avg_receiver_throughput"].mean()
    plt.plot(averages.index, averages.values, marker="o", label=algorithm)

plt.xlabel("RTT (ms)")
plt.ylabel("Receiver Throughput (Mbps)")
plt.title("TCP Algorithms: Receiver Throughput vs RTT")
plt.xticks(rtts)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/throughput_comparison.png")
plt.close()


# GRAPH 2: Average Retransmissions

plt.figure(figsize=(10, 6))

for algorithm in algorithms:
    data = df[df["algorithm"] == algorithm]
    averages = data.groupby("rtt_ms")["avg_retransmissions"].mean()
    plt.plot(averages.index, averages.values, marker="o", label=algorithm)

plt.xlabel("RTT (ms)")
plt.ylabel("Average Retransmissions")
plt.title("TCP Algorithms: Retransmissions vs RTT")
plt.xticks(rtts)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plots/retransmissions_comparison.png")
plt.close()


# GRAPH 3: Throughput vs Buffer Size

for rtt in rtts:

    plt.figure(figsize=(10, 6))

    for algorithm in algorithms:
        data = df[
            (df["algorithm"] == algorithm) &
            (df["rtt_ms"] == rtt)
        ]

        plt.plot(
            data["buffer_multiplier"],
            data["avg_receiver_throughput"],
            marker="o",
            label=algorithm
        )

    plt.xlabel("Buffer Size (BDP Multiplier)")
    plt.ylabel("Receiver Throughput (Mbps)")
    plt.title("Throughput vs Buffer Size - RTT " + str(rtt) + " ms")
    plt.xticks(buffers)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/throughput_buffer_" + str(rtt) + "ms.png")
    plt.close()


print("All comparison graphs generated successfully!")
print("Saved in the plots folder.")




(.venv) abeeha@abeeha-VirtualBox:~/cn-tcp-lab$ ls -lh plots/
total 776K
-rw-rw-r-- 1 abeeha abeeha 208K Nov 21 01:15 cwnd_vs_time.png
-rw-rw-r-- 1 abeeha abeeha  51K Nov 21 01:53 retransmissions_comparison.png
-rw-rw-r-- 1 abeeha abeeha 314K Nov 21 01:15 rtt_vs_time.png
-rw-rw-r-- 1 abeeha abeeha  45K Nov 21 01:53 throughput_buffer_100ms.png
-rw-rw-r-- 1 abeeha abeeha  45K Nov 21 01:53 throughput_buffer_20ms.png
-rw-rw-r-- 1 abeeha abeeha  46K Nov 21 01:53 throughput_buffer_50ms.png
-rw-rw-r-- 1 abeeha abeeha  54K Nov 21 01:53 throughput_comparison.png
