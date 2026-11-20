Build the Mininet Dumbbell Topology
Before writing code, let's understand what we're building.
What is a dumbbell topology?
Imagine two groups of computers communicating through two routers. The routers are connected by one central, controlled link.

Our network will look like this:
       SENDER SIDE                 RECEIVER SIDE

        h1                            h3
         \                            /
          \                          /
           R1 ===== BOTTLENECK ===== R2
          /       10 Mbps link        \
         /                             \
        h2                             h4

              20 / 50 / 100 ms RTT

Here:
- h1, h2: Sending hosts. They generate TCP traffic.
- h3, h4: Receiving hosts. They receive TCP traffic.
- R1: Left-side router.
- R2: Right-side router.
- Bottleneck: The central link connecting both routers.


Why are we building this?
Our project compares Reno, CUBIC and BBR under controlled network conditions.

We need a network where we can deliberately control:
- Available bandwidth: 10 Mbps.
- Round-trip time (RTT): 20, 50 and 100 ms.
- Buffer sizes: 0.5×, 1× and 2× bandwidth-delay product (BDP).
This allows us to compare how the three algorithms behave under identical conditions.


in dumbell.py: 
# ============================================================
# SECTION 1: IMPORT REQUIRED MININET LIBRARIES
# ============================================================

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info


# ============================================================
# SECTION 2: EXPERIMENT CONFIGURATION
# ============================================================

# Bottleneck link bandwidth in Mbps
BOTTLENECK_BW = 10

# One-way delay on the bottleneck link.
# 10ms in each direction gives approximately 20ms RTT.
ONE_WAY_DELAY = '10ms'

# Maximum queue size in packets
QUEUE_SIZE = 100


# ============================================================
# SECTION 3: CREATE DUMBBELL NETWORK TOPOLOGY
# ============================================================

class DumbbellTopo(Topo):

    def build(self, bw=10, delay='10ms', max_queue_size=100):

        # Create four end hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Create two routers
        r1 = self.addHost('r1')
        r2 = self.addHost('r2')

        # Connect Host 1 and Host 2 to Router 1
        self.addLink(
            h1, r1,
            intfName1='h1-eth0',
            intfName2='r1-eth0'
        )

        self.addLink(
            h2, r1,
            intfName1='h2-eth0',
            intfName2='r1-eth1'
        )

        # Create the central bottleneck link
        # This link controls bandwidth, delay and queue size
        self.addLink(
            r1, r2,
            intfName1='r1-eth2',
            intfName2='r2-eth0',
            bw=bw,
            delay=delay,
            max_queue_size=max_queue_size
        )

        # Connect Router 2 to Host 3 and Host 4
        self.addLink(
            r2, h3,
            intfName1='r2-eth1',
            intfName2='h3-eth0'
        )

        self.addLink(
            r2, h4,
            intfName1='r2-eth2',
            intfName2='h4-eth0'
        )


# ============================================================
# SECTION 4: CONFIGURE IP ADDRESSES
# ============================================================

def configure_network(net):

    # Get references to all network devices
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    r1 = net.get('r1')
    r2 = net.get('r2')

    # Host 1 and Router 1 network
    h1.setIP('10.0.1.2', prefixLen=24, intf='h1-eth0')
    r1.setIP('10.0.1.1', prefixLen=24, intf='r1-eth0')

    # Host 2 and Router 1 network
    h2.setIP('10.0.2.2', prefixLen=24, intf='h2-eth0')
    r1.setIP('10.0.2.1', prefixLen=24, intf='r1-eth1')

    # Central network between both routers
    r1.setIP('10.0.3.1', prefixLen=24, intf='r1-eth2')
    r2.setIP('10.0.3.2', prefixLen=24, intf='r2-eth0')

    # Router 2 and Host 3 network
    r2.setIP('10.0.4.1', prefixLen=24, intf='r2-eth1')
    h3.setIP('10.0.4.2', prefixLen=24, intf='h3-eth0')

    # Router 2 and Host 4 network
    r2.setIP('10.0.5.1', prefixLen=24, intf='r2-eth2')
    h4.setIP('10.0.5.2', prefixLen=24, intf='h4-eth0')


# ============================================================
# SECTION 5: ENABLE IP FORWARDING ON ROUTERS
# ============================================================

def configure_routers(net):

    r1 = net.get('r1')
    r2 = net.get('r2')

    # Allow Router 1 to forward packets between networks
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    # Allow Router 2 to forward packets between networks
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')


# ============================================================
# SECTION 6: CONFIGURE ROUTING TABLES
# ============================================================

def configure_routes(net):

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    r1 = net.get('r1')
    r2 = net.get('r2')

    # Configure default routes for end hosts
    h1.cmd('ip route replace default via 10.0.1.1')
    h2.cmd('ip route replace default via 10.0.2.1')

    h3.cmd('ip route replace default via 10.0.4.1')
    h4.cmd('ip route replace default via 10.0.5.1')

    # Router 1: routes to networks on the right side
    r1.cmd('ip route replace 10.0.4.0/24 via 10.0.3.2')
    r1.cmd('ip route replace 10.0.5.0/24 via 10.0.3.2')

    # Router 2: routes to networks on the left side
    r2.cmd('ip route replace 10.0.1.0/24 via 10.0.3.1')
    r2.cmd('ip route replace 10.0.2.0/24 via 10.0.3.1')


# ============================================================
# SECTION 7: START THE NETWORK
# ============================================================

def run():

    info('\n*** Creating Dumbbell Topology ***\n')

    # Create the topology with our configured bottleneck
    topo = DumbbellTopo(
        bw=BOTTLENECK_BW,
        delay=ONE_WAY_DELAY,
        max_queue_size=QUEUE_SIZE
    )

    # Create the Mininet network
    net = Mininet(
        topo=topo,
        link=TCLink,
        controller=None,
        autoSetMacs=True
    )

    try:

        # Start all hosts, routers and network links
        net.start()

        info('\n*** Configuring IP Addresses ***\n')
        configure_network(net)

        info('\n*** Enabling Router Forwarding ***\n')
        configure_routers(net)

        info('\n*** Configuring Routing Tables ***\n')
        configure_routes(net)

        info('\n*** Network Successfully Started ***\n')

        # Open Mininet command-line interface
        CLI(net)

    finally:

        # Stop the network and release its resources
        net.stop()

        info('\n*** Network Stopped ***\n')


# ============================================================
# SECTION 8: PROGRAM ENTRY POINT
# ============================================================

if __name__ == '__main__':

    # Display Mininet output in normal informational mode
    setLogLevel('info')

    # Run the network
    run()



-> actual connections : 

| Device | Connected to |
|---|---|
| h1 | r1 |
| h2 | r1 |
| r1 | r2 |
| r2 | h3 |
| r2 | h4 |

Hosts: Generate and receive TCP traffic.
Routers: Forward packets between the different networks.
Bottleneck: Restricts traffic to 10 Mbps and introduces delay.
IP addresses: Allow devices to communicate.
Routing tables: Tell devices where to send packets.

//runing by: python3 -m py_compile topology/dumbbell.py
//launch by: sudo python3 topology/dumbbell.py
//pingall
//It confirms that:
1. All four hosts can communicate with each other.
2. Both routers are forwarding packets correctly.
3. The IP addresses are configured correctly.
4. The routing tables are working.
5. The complete dumbbell topology is operational.//


run:  ip addr show r1-eth2

What does this do?
- r1 executes a command on Router 1.
- ip addr show displays network interface information.
- r1-eth2 is Router 1's connection to Router 2.//

run : r2 ip addr show r2-eth0
run: h3 iperf3 -s &

Run this at mininet>:
h1 iperf3 -c 10.0.4.2 -t 10

What does this command do?
- h1 — runs the command on Host 1.
- iperf3 — starts a network performance test.
- -c 10.0.4.2 — connects to Host 3's IP address.
- -t 10 — runs the test for 10 seconds.
What are we testing?

Traffic travels through:

h1 → r1 → BOTTLENECK → r2 → h3

//Our bottleneck is configured for 10 Mbps, so we expect throughput to be approximately 10 Mbps, although TCP overhead and other factors may make it slightly lower.
Check which TCP congestion-control algorithm is currently active
At mininet>, run:  h1 sysctl net.ipv4.tcp_congestion_control


Switch Host 1 to TCP Reno
At mininet>, run:
h1 sysctl -w net.ipv4.tcp_congestion_control=reno


reno experiment : h1 iperf3 -c 10.0.4.2 -t 30 -i 1

Switch to TCP CUBIC: 

run : h1 sysctl -w net.ipv4.tcp_congestion_control=cubic
run: h1 iperf3 -c 10.0.4.2 -t 30 -i 1
