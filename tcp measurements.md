abeeha@abeeha-VirtualBox:~/cn-tcp-lab$ grep ',RENO,' results/cwnd_rtt_timeseries.csv | head -10
2026-11-21 01:03:10.009250,RENO,0.229,10,101.31,0
2026-11-21 01:03:10.223219,RENO,0.443,10,101.334,0
2026-11-21 01:03:10.441669,RENO,0.662,20,104.593,0
2026-11-21 01:03:10.650960,RENO,0.871,66,111.802,0
2026-11-21 01:03:10.859997,RENO,1.08,192,118.462,0
2026-11-21 01:03:11.069537,RENO,1.29,360,212.685,0
2026-11-21 01:03:11.282598,RENO,1.503,506,312.179,6
2026-11-21 01:03:11.494522,RENO,1.715,307,358.928,77
2026-11-21 01:03:11.703930,RENO,1.924,260,288.767,183
2026-11-21 01:03:11.916037,RENO,2.136,189,201.818,98


abeeha@abeeha-VirtualBox:~/cn-tcp-lab$ grep ',CUBIC,' results/cwnd_rtt_timeseries.csv | head -10
2026-11-21 01:03:43.105915,CUBIC,0.223,10,101.596,0
2026-11-21 01:03:43.314340,CUBIC,0.432,10,101.71,0
2026-11-21 01:03:43.523291,CUBIC,0.641,20,104.189,0
2026-11-21 01:03:43.733024,CUBIC,0.85,58,108.474,0
2026-11-21 01:03:43.942331,CUBIC,1.06,182,117.036,0
2026-11-21 01:03:44.151796,CUBIC,1.269,336,207.081,0
2026-11-21 01:03:44.363452,CUBIC,1.481,331,303.361,5
2026-11-21 01:03:44.574565,CUBIC,1.692,240,320.882,85
2026-11-21 01:03:44.783599,CUBIC,1.901,207,225.829,60
2026-11-21 01:03:44.993270,CUBIC,2.111,183,216.706,33


abeeha@abeeha-VirtualBox:~/cn-tcp-lab$ grep ',BBR,' results/cwnd_rtt_timeseries.csv | head -10
2026-11-21 01:04:16.217504,BBR,0.222,11,101.507,0
2026-11-21 01:04:16.430717,BBR,0.435,13,101.592,0
2026-11-21 01:04:16.645596,BBR,0.65,22,104.581,0
2026-11-21 01:04:16.861816,BBR,0.866,58,102.264,0
2026-11-21 01:04:17.073017,BBR,1.077,188,106.409,0
2026-11-21 01:04:17.284659,BBR,1.289,246,180.084,0
2026-11-21 01:04:17.495768,BBR,1.5,218,258.188,28
2026-11-21 01:04:17.709858,BBR,1.714,204,254.808,42
2026-11-21 01:04:17.921445,BBR,1.926,258,252.007,0
2026-11-21 01:04:18.132104,BBR,2.136,180,111.646,0











. Summary of measurements
Metric	Reno	CUBIC	BBR
Samples	145	146	144
Minimum cwnd	10	10	4
Maximum cwnd	506	336	258
Average cwnd	156.39	165.66	172.36
Minimum RTT	101.31 ms	101.60 ms	101.51 ms
Maximum RTT	358.93 ms	320.88 ms	258.19 ms
Average RTT	191.24 ms	205.29 ms	117.27 ms


2. What do these results suggest?
Reno
- Reached the largest maximum congestion window.
- Experienced substantial RTT variation.
- Its average RTT was approximately 191 ms.
CUBIC
- Had the highest average RTT of the three.
- Reached a maximum cwnd of 336 segments.
- Showed substantial queueing delay.
BBR
- Had the highest average cwnd.
- Had the lowest average RTT: 117.27 ms.
- Its maximum RTT was also the lowest.
An interesting preliminary observation is that BBR maintained a substantially lower average RTT despite having a slightly higher average cwnd.

These are observations from one 30-second run per algorithm, not statistical conclusions across repeated experiments.

