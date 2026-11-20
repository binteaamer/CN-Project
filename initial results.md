Reno results
| Metric | Reno result |
|---|---:|
| Test duration | 30 seconds |
| Sender throughput | 10.2 Mbps |
| Receiver throughput | 9.28 Mbps |
| Retransmissions | 669 |
| Configured bottleneck | 10 Mbps |


What do these results tell us?
Throughput: The receiver achieved 9.28 Mbps, reasonably close to our 10 Mbps bottleneck capacity.

Retransmissions: Reno recorded 669 retransmissions. This is worth investigating because it indicates considerable packet retransmission activity.

Congestion window (Cwnd): It changes throughout the experiment as Reno responds to network conditions.

One interesting observation: several one-second intervals show 14.7 Mbps followed by zero throughput. This bursty pattern means we should investigate the measurements before treating them as final experimental results.

We'll eventually repeat experiments and save the raw measurements.

cubic results:
| Metric | CUBIC |
|---|---:|
| Test duration | 30 seconds |
| Sender throughput | 9.71 Mbps |
| Receiver throughput | 9.31 Mbps |
| Retransmissions | 34 |
| Bottleneck capacity | 10 Mbps |


Reno vs CUBIC comparison:| Metric | Reno | CUBIC |
|---|---:|---:|
| Sender throughput | 10.2 Mbps | 9.71 Mbps |
| Receiver throughput | 9.28 Mbps | 9.31 Mbps |
| Retransmissions | 669 | 34 |

3. What can we observe?
Throughput: Both algorithms achieved almost identical receiver throughput.

Retransmissions: Reno recorded 669, whereas CUBIC recorded only 34.


| Metric | Reno | CUBIC | BBR |
|---|---:|---:|---:|
| Sender throughput | 10.2 Mbps | 9.71 Mbps | 9.33 Mbps |
| Receiver throughput | 9.28 Mbps | 9.31 Mbps | 9.14 Mbps |
| Retransmissions | 669 | 34 | 0 |
| Duration | 30 sec | 30 sec | 30 sec |



. What have we learned?
Throughput: All three algorithms achieved approximately 9.1–9.3 Mbps receiver throughput. This is close to our 10 Mbps bottleneck capacity.

Retransmissions:
- Reno: 669
- CUBIC: 34
- BBR: 0
BBR achieved the fewest retransmissions in these particular runs.

However, zero retransmissions does not automatically mean zero packet loss. We should also examine packet captures and repeat the experiments before drawing final conclusions.
Congestion window: CUBIC gradually increased its congestion window, with reductions when congestion was detected.

These are preliminary observations from one run each, not final conclusions. We'll need repeated runs for reliable comparisons.

