reno retransmission distribution
Time interval	Retransmissions
0–1 seconds	0
1–2 seconds	0
2–3 seconds	99
3–4 seconds	136
4–5 seconds	1
Total	236


Interpretation
- Reno had no detected retransmissions during its first two seconds.
- Retransmissions increased sharply during seconds 2–4.
- 235 out of 236 retransmissions (99.6%) occurred between seconds 2 and 4.
- Activity then almost completely stopped.
This indicates a concentrated loss-recovery episode rather than retransmissions being evenly distributed throughout the test.



What we've learned
- Reno: Significant retransmission and duplicate ACK activity.
- CUBIC: Very few detected retransmissions, but duplicate ACK activity was present.
- BBR: No retransmissions or duplicate ACKs detected in this particular capture.
These are packet-analysis observations from individual runs, not proof that BBR never experiences packet loss.
Packet analysis progress
We've successfully captured and analyzed all three algorithms:
1. Packet captures verified.
2. Retransmissions counted.
3. Retransmission timestamps examined.
4. Retransmissions grouped by second for Reno and CUBIC.
5. Duplicate ACKs counted for all three.
