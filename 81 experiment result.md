easurement.run_experiment

===================================
TCP CONGESTION CONTROL EXPERIMENT
===================================
Algorithms: ['reno', 'cubic', 'bbr']
RTT values: [20, 50, 100]
Buffer multipliers: [0.5, 1, 2]
Test duration: 30
Repetitions: 3

===================================
NEW NETWORK CONFIGURATION
RTT: 20 ms
Buffer: 0.5 x BDP
Queue: 8 packets
===================================

Starting Mininet topology...
Target RTT: 20 ms
Queue size: 8 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:00:18', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.352, 'receiver_throughput_mbps': 8.275, 'retransmissions': 149}
Progress: 1 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:00:53', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.282, 'receiver_throughput_mbps': 8.206, 'retransmissions': 136}
Progress: 2 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:01:28', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.388, 'receiver_throughput_mbps': 8.31, 'retransmissions': 132}
Progress: 3 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:02:04', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.493, 'receiver_throughput_mbps': 8.416, 'retransmissions': 120}
Progress: 4 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:02:39', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.492, 'receiver_throughput_mbps': 8.415, 'retransmissions': 121}
Progress: 5 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:03:15', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.422, 'receiver_throughput_mbps': 8.346, 'retransmissions': 126}
Progress: 6 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:03:50', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.218, 'retransmissions': 717}
Progress: 7 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:04:25', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 9.365, 'receiver_throughput_mbps': 9.252, 'retransmissions': 743}
Progress: 8 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 20 ms
Buffer: 0.5 x BDP
Queue size: 8 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:05:01', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 0.5, 'queue_size': 8, 'sender_throughput_mbps': 8.946, 'receiver_throughput_mbps': 8.798, 'retransmissions': 680}
Progress: 9 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 20 ms
Buffer: 1 x BDP
Queue: 17 packets
===================================

Starting Mininet topology...
Target RTT: 20 ms
Queue size: 17 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:05:37', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.216, 'retransmissions': 134}
Progress: 10 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:06:12', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.251, 'retransmissions': 107}
Progress: 11 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:06:47', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.283, 'retransmissions': 97}
Progress: 12 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:07:22', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.47, 'receiver_throughput_mbps': 9.317, 'retransmissions': 103}
Progress: 13 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:07:58', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.212, 'retransmissions': 120}
Progress: 14 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:08:33', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.285, 'retransmissions': 91}
Progress: 15 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:09:08', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.249, 'retransmissions': 54}
Progress: 16 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:09:43', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.214, 'retransmissions': 56}
Progress: 17 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 20 ms
Buffer: 1 x BDP
Queue size: 17 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:10:19', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 1, 'queue_size': 17, 'sender_throughput_mbps': 9.366, 'receiver_throughput_mbps': 9.179, 'retransmissions': 74}
Progress: 18 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 20 ms
Buffer: 2 x BDP
Queue: 33 packets
===================================

Starting Mininet topology...
Target RTT: 20 ms
Queue size: 33 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:10:55', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.786, 'receiver_throughput_mbps': 9.303, 'retransmissions': 194}
Progress: 19 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:11:30', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.681, 'receiver_throughput_mbps': 9.27, 'retransmissions': 185}
Progress: 20 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:12:06', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.68, 'receiver_throughput_mbps': 9.282, 'retransmissions': 196}
Progress: 21 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:12:41', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.338, 'retransmissions': 69}
Progress: 22 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:13:16', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.436, 'receiver_throughput_mbps': 9.305, 'retransmissions': 72}
Progress: 23 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:13:52', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.402, 'receiver_throughput_mbps': 9.305, 'retransmissions': 19}
Progress: 24 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:14:27', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.211, 'retransmissions': 0}
Progress: 25 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:15:02', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.227, 'receiver_throughput_mbps': 9.072, 'retransmissions': 0}
Progress: 26 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 20 ms
Buffer: 2 x BDP
Queue size: 33 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:15:38', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 20, 'buffer_multiplier': 2, 'queue_size': 33, 'sender_throughput_mbps': 9.401, 'receiver_throughput_mbps': 9.247, 'retransmissions': 0}
Progress: 27 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 50 ms
Buffer: 0.5 x BDP
Queue: 21 packets
===================================

Starting Mininet topology...
Target RTT: 50 ms
Queue size: 21 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:16:14', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 8.947, 'receiver_throughput_mbps': 8.721, 'retransmissions': 99}
Progress: 28 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:16:50', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 8.842, 'receiver_throughput_mbps': 8.652, 'retransmissions': 99}
Progress: 29 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:17:25', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 8.912, 'receiver_throughput_mbps': 8.652, 'retransmissions': 99}
Progress: 30 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:18:00', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.296, 'receiver_throughput_mbps': 9.069, 'retransmissions': 133}
Progress: 31 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:18:36', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.366, 'receiver_throughput_mbps': 9.175, 'retransmissions': 106}
Progress: 32 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:19:11', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.367, 'receiver_throughput_mbps': 9.17, 'retransmissions': 97}
Progress: 33 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:19:47', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.541, 'receiver_throughput_mbps': 9.136, 'retransmissions': 94}
Progress: 34 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:20:22', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.138, 'retransmissions': 174}
Progress: 35 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 50 ms
Buffer: 0.5 x BDP
Queue size: 21 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:20:58', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 0.5, 'queue_size': 21, 'sender_throughput_mbps': 9.611, 'receiver_throughput_mbps': 9.17, 'retransmissions': 192}
Progress: 36 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 50 ms
Buffer: 1 x BDP
Queue: 42 packets
===================================

Starting Mininet topology...
Target RTT: 50 ms
Queue size: 42 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:21:34', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.681, 'receiver_throughput_mbps': 9.259, 'retransmissions': 99}
Progress: 37 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:22:10', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.681, 'receiver_throughput_mbps': 9.305, 'retransmissions': 184}
Progress: 38 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:22:45', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.855, 'receiver_throughput_mbps': 9.272, 'retransmissions': 201}
Progress: 39 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:23:21', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.541, 'receiver_throughput_mbps': 9.3, 'retransmissions': 117}
Progress: 40 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:23:56', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.678, 'receiver_throughput_mbps': 9.296, 'retransmissions': 104}
Progress: 41 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:24:32', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.541, 'receiver_throughput_mbps': 9.262, 'retransmissions': 131}
Progress: 42 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:25:07', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.099, 'retransmissions': 26}
Progress: 43 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:25:43', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.032, 'retransmissions': 24}
Progress: 44 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 50 ms
Buffer: 1 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:26:18', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 1, 'queue_size': 42, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.136, 'retransmissions': 52}
Progress: 45 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 50 ms
Buffer: 2 x BDP
Queue: 83 packets
===================================

Starting Mininet topology...
Target RTT: 50 ms
Queue size: 83 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:26:55', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 10.135, 'receiver_throughput_mbps': 9.286, 'retransmissions': 438}
Progress: 46 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:27:31', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 10.345, 'receiver_throughput_mbps': 9.317, 'retransmissions': 428}
Progress: 47 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:28:06', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 10.135, 'receiver_throughput_mbps': 9.283, 'retransmissions': 416}
Progress: 48 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:28:42', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.541, 'receiver_throughput_mbps': 9.202, 'retransmissions': 27}
Progress: 49 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:29:18', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.576, 'receiver_throughput_mbps': 9.309, 'retransmissions': 37}
Progress: 50 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:29:53', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.61, 'receiver_throughput_mbps': 9.253, 'retransmissions': 36}
Progress: 51 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:30:29', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.541, 'receiver_throughput_mbps': 9.136, 'retransmissions': 0}
Progress: 52 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:31:04', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.506, 'receiver_throughput_mbps': 9.171, 'retransmissions': 0}
Progress: 53 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 50 ms
Buffer: 2 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:31:40', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 50, 'buffer_multiplier': 2, 'queue_size': 83, 'sender_throughput_mbps': 9.505, 'receiver_throughput_mbps': 9.17, 'retransmissions': 0}
Progress: 54 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 100 ms
Buffer: 0.5 x BDP
Queue: 42 packets
===================================

Starting Mininet topology...
Target RTT: 100 ms
Queue size: 42 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:32:17', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.052, 'receiver_throughput_mbps': 8.602, 'retransmissions': 160}
Progress: 55 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:32:52', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.261, 'receiver_throughput_mbps': 8.729, 'retransmissions': 150}
Progress: 56 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:33:28', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 8.911, 'receiver_throughput_mbps': 8.392, 'retransmissions': 167}
Progress: 57 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:34:04', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.576, 'receiver_throughput_mbps': 9.19, 'retransmissions': 221}
Progress: 58 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:34:40', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.575, 'receiver_throughput_mbps': 9.02, 'retransmissions': 189}
Progress: 59 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:35:16', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.331, 'receiver_throughput_mbps': 8.983, 'retransmissions': 181}
Progress: 60 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:35:51', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.855, 'receiver_throughput_mbps': 9.055, 'retransmissions': 276}
Progress: 61 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:36:27', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.891, 'receiver_throughput_mbps': 9.017, 'retransmissions': 246}
Progress: 62 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 100 ms
Buffer: 0.5 x BDP
Queue size: 42 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:37:03', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 0.5, 'queue_size': 42, 'sender_throughput_mbps': 9.926, 'receiver_throughput_mbps': 9.046, 'retransmissions': 184}
Progress: 63 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 100 ms
Buffer: 1 x BDP
Queue: 83 packets
===================================

Starting Mininet topology...
Target RTT: 100 ms
Queue size: 83 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:37:40', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 10.31, 'receiver_throughput_mbps': 9.229, 'retransmissions': 379}
Progress: 64 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:38:16', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.681, 'receiver_throughput_mbps': 8.809, 'retransmissions': 265}
Progress: 65 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:38:52', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 10.203, 'receiver_throughput_mbps': 9.229, 'retransmissions': 372}
Progress: 66 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:39:28', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.89, 'receiver_throughput_mbps': 9.203, 'retransmissions': 195}
Progress: 67 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:40:04', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.82, 'receiver_throughput_mbps': 9.2, 'retransmissions': 218}
Progress: 68 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:40:40', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.751, 'receiver_throughput_mbps': 9.239, 'retransmissions': 204}
Progress: 69 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:41:16', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.856, 'receiver_throughput_mbps': 9.123, 'retransmissions': 80}
Progress: 70 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:41:52', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.855, 'receiver_throughput_mbps': 9.053, 'retransmissions': 80}
Progress: 71 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 100 ms
Buffer: 1 x BDP
Queue size: 83 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:42:28', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 1, 'queue_size': 83, 'sender_throughput_mbps': 9.855, 'receiver_throughput_mbps': 9.054, 'retransmissions': 80}
Progress: 72 / 81

Stopping Mininet network...

===================================
NEW NETWORK CONFIGURATION
RTT: 100 ms
Buffer: 2 x BDP
Queue: 167 packets
===================================

Starting Mininet topology...
Target RTT: 100 ms
Queue size: 167 packets
Network started successfully.

-----------------------------------
Algorithm: RENO
Repetition: 1
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:43:05', 'algorithm': 'RENO', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 11.254, 'receiver_throughput_mbps': 9.238, 'retransmissions': 858}
Progress: 73 / 81

-----------------------------------
Algorithm: RENO
Repetition: 2
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:43:42', 'algorithm': 'RENO', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 11.567, 'receiver_throughput_mbps': 9.236, 'retransmissions': 855}
Progress: 74 / 81

-----------------------------------
Algorithm: RENO
Repetition: 3
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:44:18', 'algorithm': 'RENO', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 11.219, 'receiver_throughput_mbps': 9.203, 'retransmissions': 841}
Progress: 75 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 1
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:44:54', 'algorithm': 'CUBIC', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.961, 'receiver_throughput_mbps': 9.128, 'retransmissions': 36}
Progress: 76 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 2
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:45:31', 'algorithm': 'CUBIC', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.82, 'receiver_throughput_mbps': 9.221, 'retransmissions': 71}
Progress: 77 / 81

-----------------------------------
Algorithm: CUBIC
Repetition: 3
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:46:07', 'algorithm': 'CUBIC', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.995, 'receiver_throughput_mbps': 9.179, 'retransmissions': 42}
Progress: 78 / 81

-----------------------------------
Algorithm: BBR
Repetition: 1
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:46:43', 'algorithm': 'BBR', 'repetition': 1, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.75, 'receiver_throughput_mbps': 9.052, 'retransmissions': 0}
Progress: 79 / 81

-----------------------------------
Algorithm: BBR
Repetition: 2
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:47:18', 'algorithm': 'BBR', 'repetition': 2, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.821, 'receiver_throughput_mbps': 9.053, 'retransmissions': 0}
Progress: 80 / 81

-----------------------------------
Algorithm: BBR
Repetition: 3
RTT: 100 ms
Buffer: 2 x BDP
Queue size: 167 packets
-----------------------------------

Experiment result:
{'date': '2026-11-20 23:47:54', 'algorithm': 'BBR', 'repetition': 3, 'duration_seconds': 30, 'bandwidth_mbps': 10, 'rtt_ms': 100, 'buffer_multiplier': 2, 'queue_size': 167, 'sender_throughput_mbps': 9.856, 'receiver_throughput_mbps': 9.053, 'retransmissions': 0}
Progress: 81 / 81

Stopping Mininet network...

===================================
ALL EXPERIMENTS COMPLETED
===================================
Completed: 81 / 81
CSV file: results/tcp_matrix_results.csv
abeeha@abeeha-VirtualBox:~/cn-tcp-lab$ 
