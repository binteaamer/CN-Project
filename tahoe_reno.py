import matplotlib.pyplot as plt


def simulate_tcp(algorithm, total_rounds, loss_rounds):
    cwnd = 1
    ssthresh = 16

    rounds = []
    cwnd_values = []
    states = []

    state = "Slow Start"

    for round_num in range(1, total_rounds + 1):

        rounds.append(round_num)
        cwnd_values.append(cwnd)
        states.append(state)

        print(algorithm, "| Round:", round_num,
              "| CWND:", cwnd,
              "| SSTHRESH:", ssthresh,
              "| State:", state)

        if round_num in loss_rounds:

            print("Packet loss detected!")

            ssthresh = max(cwnd // 2, 2)

            if algorithm == "Tahoe":
                cwnd = 1
                state = "Slow Start"

            else:
                cwnd = ssthresh
                state = "Congestion Avoidance"

        elif state == "Slow Start":

            cwnd = cwnd * 2

            if cwnd >= ssthresh:
                state = "Congestion Avoidance"

        elif state == "Congestion Avoidance":

            cwnd = cwnd + 1

    return rounds, cwnd_values


total_rounds = 25
loss_rounds = [8, 17]

print("\n========== TCP TAHOE ==========")
tahoe_rounds, tahoe_cwnd = simulate_tcp(
    "Tahoe", total_rounds, loss_rounds
)

print("\n========== TCP RENO ==========")
reno_rounds, reno_cwnd = simulate_tcp(
    "Reno", total_rounds, loss_rounds
)


plt.figure(figsize=(10, 6))

plt.plot(tahoe_rounds, tahoe_cwnd, marker='o', label="TCP Tahoe")
plt.plot(reno_rounds, reno_cwnd, marker='s', label="TCP Reno")

plt.xlabel("Transmission Round")
plt.ylabel("Congestion Window (Segments)")
plt.title("TCP Tahoe vs TCP Reno Congestion Control")

plt.legend()
plt.grid(True)

plt.savefig("plots/tahoe_vs_reno.png")
plt.show()

print("\nGraph saved: plots/tahoe_vs_reno.png")
