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






















Comparions :


ALGORITHM | RTT | BUFFER | AVG RECEIVER Mbps | AVG SENDER Mbps | AVG RETRANSMISSIONS
-----------------------------------------------------------------------------------------------
BBR      | 20 ms | 0.5 x |             9.089 |           9.237 | 713.3
CUBIC    | 20 ms | 0.5 x |             8.392 |           8.469 | 122.3
RENO     | 20 ms | 0.5 x |             8.264 |           8.341 | 139.0
BBR      | 20 ms | 1   x |             9.214 |           9.389 | 61.3
CUBIC    | 20 ms | 1   x |             9.271 |           9.459 | 104.7
RENO     | 20 ms | 1   x |             9.250 |           9.436 | 112.7
BBR      | 20 ms | 2   x |             9.177 |           9.343 | 0.0
CUBIC    | 20 ms | 2   x |             9.316 |           9.448 | 53.3
RENO     | 20 ms | 2   x |             9.285 |           9.716 | 191.7
BBR      | 50 ms | 0.5 x |             9.148 |           9.553 | 153.3
CUBIC    | 50 ms | 0.5 x |             9.138 |           9.343 | 112.0
RENO     | 50 ms | 0.5 x |             8.675 |           8.900 | 99.0
BBR      | 50 ms | 1   x |             9.089 |           9.506 | 34.0
CUBIC    | 50 ms | 1   x |             9.286 |           9.587 | 117.3
RENO     | 50 ms | 1   x |             9.279 |           9.739 | 161.3
BBR      | 50 ms | 2   x |             9.159 |           9.517 | 0.0
CUBIC    | 50 ms | 2   x |             9.255 |           9.576 | 33.3
RENO     | 50 ms | 2   x |             9.295 |          10.205 | 427.3
BBR      | 100ms | 0.5 x |             9.039 |           9.891 | 235.3
CUBIC    | 100ms | 0.5 x |             9.064 |           9.494 | 197.0
RENO     | 100ms | 0.5 x |             8.574 |           9.075 | 159.0
BBR      | 100ms | 1   x |             9.077 |           9.855 | 80.0
CUBIC    | 100ms | 1   x |             9.214 |           9.820 | 205.7
RENO     | 100ms | 1   x |             9.089 |          10.065 | 338.7
BBR      | 100ms | 2   x |             9.053 |           9.809 | 0.0
CUBIC    | 100ms | 2   x |             9.176 |           9.925 | 49.7
RENO     | 100ms | 2   x |             9.226 |          11.347 | 851.3



et's interpret what the results are telling us before making graphs.
1. Initial observations
Receiver throughput
Receiver throughput is our main metric for comparing how much useful data actually reached the destination.
- CUBIC: Generally performs consistently, with averages around 8.39–9.32 Mbps.
- RENO: Performs relatively poorly with smaller buffers, especially at 100 ms RTT and 0.5× BDP (8.574 Mbps).
- BBR: Usually achieves around 9 Mbps, but its results need closer inspection.
Retransmissions
Some interesting patterns:
- Reno reaches an average of 851.3 retransmissions at 100 ms RTT and 2× BDP.
- CUBIC records 49.7 retransmissions in the same configuration.
- BBR records zero retransmissions at 2× BDP across all three RTT values.
- However, BBR records 713.3 retransmissions at 20 ms RTT and 0.5× BDP. This is an unusual result that we should investigate.
2. One important issue to investigate
Look at these sender throughput averages:
Algorithm	RTT	Buffer	Sender throughput
Reno	100 ms	2×	11.347 Mbps
Reno	50 ms	2×	10.205 Mbps
CUBIC	100 ms	2×	9.925 Mbps


Our configured bottleneck is 10 Mbps.

Sender throughput exceeding 10 Mbps is worth investigating. It doesn't automatically mean the experiment failed, but we should understand how the script measures sender and receiver throughput before using these figures in the report.



. Why sender throughput can exceed 10 Mbps
The configured bottleneck is 10 Mbps, but sum_sent is not necessarily equivalent to useful data delivered across the bottleneck.

Retransmissions, measurement intervals and traffic shaping can affect the relationship between sender and receiver measurements.

For our main comparison, we'll use receiver throughput as goodput and report sender throughput separately.

However, we should investigate the unusually high Reno retransmissions and BBR's results rather than assume they are expected.





. Final diagnostic comparison
Configuration
- Bottleneck: 10 Mbps
- RTT: 100 ms
- Queue size: 167 packets (2×BDP)
- Duration: 10 seconds
Measurement	Reno	CUBIC	BBR
Sender throughput (Mbps)	16.247	11.007	11.112
Receiver throughput (Mbps)	9.015	8.877	9.022
iperf3 retransmissions	853	27	0
R1 queue drops	417	19	0
R2 queue drops	0	0	0


Note: Reno's queue-drop count comes from its earlier packet-capture diagnostic; CUBIC and BBR counts come from their respective diagnostic runs.
2. What can we conclude?
Reno
- Highest retransmission count.
- Highest observed queue drops.
- Receiver throughput around 9 Mbps.
CUBIC
- Much fewer retransmissions than Reno.
- Only 19 queue drops.
- Similar receiver throughput.
BBR
- No reported retransmissions.
- No observed queue drops.
- Highest receiver throughput among these three runs, although the difference is very small.
Interesting finding: BBR achieved approximately 9 Mbps without queue drops in this particular test. This is consistent with BBR's model-based congestion-control approach, which aims to estimate bottleneck bandwidth and round-trip propagation time.

However, these are individual diagnostic runs. We should not present them as statistically conclusive evidence.
3. Where we stand in the project
Completed:
- Ubuntu and Mininet setup.
- Dumbbell topology.
- 81-experiment matrix.
- CSV validation and backup.
- Reno packet-capture analysis.
- Reno, CUBIC and BBR diagnostic comparisons.
- Bottleneck queue-drop measurements.
Still pending:
- Congestion window (cwnd) and RTT measurements over time.
- Competing TCP flows.
- Jain's fairness index.
- Tahoe vs Reno simulator.
- Graphs, statistical analysis and final report.
