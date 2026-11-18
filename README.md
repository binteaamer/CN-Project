# ⚡ TCP CONGESTION CONTROL LAB

<div align="center">

### `RENO` · `CUBIC` · `BBR`

**Measuring TCP congestion control under controlled network conditions.**

![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Mininet](https://img.shields.io/badge/Mininet-Network_Emulation-black)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

`[ COMPUTER NETWORKS ]` `[ LINUX ]` `[ NETWORK MEASUREMENT ]`

</div>

---

## `01 // OVERVIEW`

What happens when different TCP congestion control algorithms compete for the same bottleneck?

This project compares three Linux TCP congestion control algorithms:

- **Reno:** Loss-based AIMD congestion control.
- **CUBIC:** Loss-based algorithm with cubic congestion-window growth.
- **BBR:** Model-based congestion control.

Using Mininet and real TCP traffic, we investigate throughput, congestion windows, latency, retransmissions and bandwidth fairness.

## `02 // NETWORK ARCHITECTURE`

A Dumbbell Topology implemented using Mininet.

```text
       LEFT LAN                  RIGHT LAN

      +------+                   +------+
      |  h1  |                   |  h3  |
      +--+---+                   +---+--+
         |                           |
      +--+---+                   +---+--+
      |  h2  |                   |  h4  |
      +--+---+                   +---+--+
         |                           |
      +--+---+=================+---+--+
      |  R1  |   BOTTLENECK     |  R2  |
      +------+=================+------+
```

## `03 // TECH STACK`

| Technology | Purpose |
|---|---|
| Ubuntu 24.04 | Linux environment |
| Mininet | Network emulation |
| Python 3 | Simulation and automation |
| iperf3 | TCP traffic generation |
| `ss` / `tc` | TCP monitoring and traffic shaping |
| tcpdump | Packet capture |
| Wireshark | Packet analysis |
| NumPy / Pandas | Data processing |
| Matplotlib / Seaborn | Visualization |

## `04 // EXPERIMENTS`

**E1 — Single Flow**

Compare Reno, CUBIC and BBR across different RTTs and buffer sizes.

`3 algorithms × 3 RTTs × 3 buffers × 3 runs = 81 runs`

**E2 — TCP Competition**

Evaluate bandwidth sharing and fairness between competing TCP flows.

`3 combinations × 2 RTT setups × 3 buffers × 3 runs = 54 runs`

**E3 — Tahoe vs Reno**

Develop a Python event-driven simulator and compare its output with actual Linux Reno measurements.

## `05 // PERFORMANCE METRICS`

- Congestion Window (`cwnd`)
- Throughput and link utilization
- RTT and queueing delay
- TCP retransmissions
- Jain's Fairness Index
- Mean and standard deviation

### Jain's Fairness Index

\[
J(x)=\frac{(\sum x_i)^2}{n\sum x_i^2}
\]

`J = 1.0` indicates perfect fairness.

## `06 // EXPERIMENTAL PIPELINE`

```text
       MININET TOPOLOGY
              |
       TCP TRAFFIC (iperf3)
              |
      +-------+-------+
      |       |       |
    CWND     RTT    PACKETS
      |       |       |
      +-------+-------+
              |
        CSV / PCAPNG
              |
       PYTHON ANALYSIS
              |
       GRAPHS & RESULTS
```

## `07 // SETUP`

### Clone repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>
```

### Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install numpy pandas matplotlib seaborn scipy jupyter
```

### Mininet installation

```bash
git clone https://github.com/mininet/mininet.git
cd mininet
sudo util/install.sh -fnv
```

### Verify

```bash
sudo mn --test pingall
```

## `08 // ROADMAP`

- [x] Ubuntu environment preparation
- [x] Python virtual environment
- [x] Networking tools installation commands
- [ ] Verify Reno, CUBIC and BBR
- [ ] Install and test Mininet
- [ ] Build dumbbell topology
- [ ] Configure bottleneck and routing
- [ ] Develop CWND / RTT sampler
- [ ] Run TCP experiments
- [ ] Implement Tahoe vs Reno simulator
- [ ] Analyse packet captures
- [ ] Generate graphs and final report

## `09 // TEAM`

| Member | Roll Number |
|---|---|
| Abeeha Binte Aamer | 24K-0940 |
| Aamna Rizwan | 24K-0695 |
| Laiba Khan | 24K-0644 |

**Course:** Computer Networks — 5F  
**Instructor:** Sir Usama Auntley

---

<div align="center">

```text
$ echo "Packets don't lie. Measurements matter."
```

`[ TCP ]` `[ LINUX ]` `[ MININET ]` `[ PYTHON ]`

**END OF TRANSMISSION**

</div>
