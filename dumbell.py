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

BOTTLENECK_BW = 10
ONE_WAY_DELAY = '10ms'
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

        # Central bottleneck link
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

    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

    r1 = net.get('r1')
    r2 = net.get('r2')

    # Host 1 and Router 1
    h1.setIP('10.0.1.2', prefixLen=24, intf='h1-eth0')
    r1.setIP('10.0.1.1', prefixLen=24, intf='r1-eth0')

    # Host 2 and Router 1
    h2.setIP('10.0.2.2', prefixLen=24, intf='h2-eth0')
    r1.setIP('10.0.2.1', prefixLen=24, intf='r1-eth1')

    # Central router network
    r1.setIP('10.0.3.1', prefixLen=24, intf='r1-eth2')
    r2.setIP('10.0.3.2', prefixLen=24, intf='r2-eth0')

    # Router 2 and Host 3
    r2.setIP('10.0.4.1', prefixLen=24, intf='r2-eth1')
    h3.setIP('10.0.4.2', prefixLen=24, intf='h3-eth0')

    # Router 2 and Host 4
    r2.setIP('10.0.5.1', prefixLen=24, intf='r2-eth2')
    h4.setIP('10.0.5.2', prefixLen=24, intf='h4-eth0')


# ============================================================
# SECTION 5: ENABLE IP FORWARDING
# ============================================================

def configure_routers(net):

    r1 = net.get('r1')
    r2 = net.get('r2')

    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
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

    # Default routes for end hosts
    h1.cmd('ip route replace default via 10.0.1.1')
    h2.cmd('ip route replace default via 10.0.2.1')

    h3.cmd('ip route replace default via 10.0.4.1')
    h4.cmd('ip route replace default via 10.0.5.1')

    # Routes from Router 1 to the right-side networks
    r1.cmd('ip route replace 10.0.4.0/24 via 10.0.3.2')
    r1.cmd('ip route replace 10.0.5.0/24 via 10.0.3.2')

    # Routes from Router 2 to the left-side networks
    r2.cmd('ip route replace 10.0.1.0/24 via 10.0.3.1')
    r2.cmd('ip route replace 10.0.2.0/24 via 10.0.3.1')


# ============================================================
# SECTION 7: START THE NETWORK
# ============================================================

def run():

    info('\n*** Creating Dumbbell Topology ***\n')

    topo = DumbbellTopo(
        bw=BOTTLENECK_BW,
        delay=ONE_WAY_DELAY,
        max_queue_size=QUEUE_SIZE
    )

    net = Mininet(
        topo=topo,
        link=TCLink,
        controller=None,
        autoSetMacs=True
    )

    try:

        net.start()

        info('\n*** Configuring IP Addresses ***\n')
        configure_network(net)

        info('\n*** Enabling Router Forwarding ***\n')
        configure_routers(net)

        info('\n*** Configuring Routing Tables ***\n')
        configure_routes(net)

        info('\n*** Network Successfully Started ***\n')

        CLI(net)

    finally:

        net.stop()

        info('\n*** Network Stopped ***\n')


# ============================================================
# SECTION 8: PROGRAM ENTRY POINT
# ============================================================

if __name__ == '__main__':

    setLogLevel('info')

    run()
