1. One-Time Ubuntu Setup

Open Ubuntu Terminal using Ctrl + Alt + T.

Update Ubuntu

sudo apt update
sudo apt full-upgrade -y
sudo reboot

Install Development and Networking Tools

sudo apt install -y \
git curl wget vim nano tmux tree unzip \
python3 python3-pip python3-venv python3-dev build-essential \
iproute2 iputils-ping traceroute net-tools \
tcpdump tshark wireshark iperf3 ethtool jq

For the Wireshark prompt, select Yes.

Add Wireshark Capture Permission

sudo usermod -aG wireshark "$USER"

Reboot:

sudo reboot

Verify the group:

groups

wireshark must appear in the output.

2. Python Environment Setup

Create the project directory and virtual environment:

mkdir -p ~/cn-tcp-lab
cd ~/cn-tcp-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib seaborn scipy jupyter
python -m pip check

Create Project Directories

mkdir -p topology measurement experiments simulator analysis results captures plots tables

Activate This Environment Later

Whenever you open a new terminal:

cd ~/cn-tcp-lab
source .venv/bin/activate

3. Mininet and Open vSwitch Setup

Do not run the legacy source installer again.

Install Mininet and Open vSwitch:

sudo apt install -y mininet openvswitch-switch
sudo systemctl enable --now openvswitch-switch
sudo mn -c

4. Enable BBR

Load BBR

sudo modprobe tcp_bbr

Make It Load Automatically

echo tcp_bbr | sudo tee /etc/modules-load.d/tcp-bbr.conf

Verify Available Congestion-Control Algorithms

sysctl net.ipv4.tcp_available_congestion_control

The output must contain:

reno cubic bbr

Check the Default Algorithm

sysctl net.ipv4.tcp_congestion_control

Do not change the default algorithm permanently unless required.

5. Full Environment Verification

Run these commands from the project directory.

cd ~/cn-tcp-lab
source .venv/bin/activate

Python Verification

python --version
python -c "import numpy, pandas, matplotlib, seaborn, scipy, jupyter; print('Python libraries: OK')"
python -m pip check

Expected output:

Python 3.12.x
Python libraries: OK
No broken requirements found.

Network-Tool Verification

python3 --version
iperf3 --version
tshark --version
tcpdump --version
ip -V
tc -V
mn --version
ovs-vsctl --version

Open vSwitch Verification

sudo systemctl status openvswitch-switch --no-pager
sudo ovs-vsctl show

Open vSwitch should show:

Active: active (exited)

Mininet Verification

sudo mn -c
sudo mn --switch ovsbr --controller none --test pingall

The result must contain:

*** Results: 0% dropped

Clean up afterward:

sudo mn -c

6. iperf3 Verification

Terminal 1 — Start the Server

iperf3 -s

Keep this terminal open. It should show:

Server listening on 5201

Terminal 2 — Run the Tests

iperf3 -c 127.0.0.1 -t 3 -C reno
iperf3 -c 127.0.0.1 -t 3 -C cubic
iperf3 -c 127.0.0.1 -t 3 -C bbr

Let every test finish naturally. Do not press Ctrl + C during a test.

Stop the server in Terminal 1 using Ctrl + C.

Note: Loopback throughput should be very high. This verifies the tools, not the project's 10 Mbps bottleneck.

7. Packet-Capture Verification

Create a Three-Second Loopback Capture

cd ~/cn-tcp-lab
mkdir -p captures
dumpcap -i lo -a duration:3 -w captures/tcpdump-test.pcapng
capinfos captures/tcpdump-test.pcapng

Open the Capture in Wireshark

wireshark captures/tcpdump-test.pcapng

The capture should exist and report packets captured.

Generate a Larger Capture

Terminal 1 — Start the iperf3 Server

iperf3 -s

Terminal 2 — Start Packet Capture

dumpcap -i lo -a duration:5 -w ~/cn-tcp-lab/captures/iperf-test.pcapng

Terminal 3 — Generate Traffic

iperf3 -c 127.0.0.1 -t 5

Stop the iperf3 server in Terminal 1 afterward.

8. VirtualBox Snapshot

When everything passes, shut down Ubuntu:

sudo shutdown now

In VirtualBox Manager:

Ubuntu VM → Machine → Take Snapshot

Snapshot name:

Verified CN Lab Environment

Description:

Ubuntu 24.04, Python 3.12 environment, Mininet 2.3.0,
Open vSwitch 3.3.9, iperf3, Wireshark, Reno/CUBIC/BBR verified.

Recommended VirtualBox Settings

RAM: 8 GB

CPUs: 4

Disk: 40–60 GB

Network adapter: NAT

Take this snapshot before project implementation.

Restore the Snapshot Later

Ubuntu VM → Snapshots → Verified CN Lab Environment → Restore

9. Starting Setup from the Snapshot

After restoring the snapshot or rebooting Ubuntu:

cd ~/cn-tcp-lab
source .venv/bin/activate
sudo modprobe tcp_bbr
sudo systemctl enable --now openvswitch-switch
sudo mn -c

Quick Verification

sysctl net.ipv4.tcp_available_congestion_control
sudo mn --switch ovsbr --controller none --test pingall

This should show Reno, CUBIC, and BBR, and 0% packet loss.

10. Commands for Demonstration

Run these commands at the beginning of a demonstration.

Activate the Environment

cd ~/cn-tcp-lab
source .venv/bin/activate
sudo systemctl status openvswitch-switch --no-pager

Show the Environment

uname -a
mn --version
ovs-vsctl --version
iperf3 --version
python --version
sysctl net.ipv4.tcp_available_congestion_control
sysctl net.ipv4.tcp_congestion_control

Show Mininet

sudo mn -c
sudo mn --switch ovsbr --controller none --test pingall
sudo mn -c

Show Reno, CUBIC, and BBR

Start the server:

iperf3 -s

In another terminal:

iperf3 -c 127.0.0.1 -t 2 -C reno
iperf3 -c 127.0.0.1 -t 2 -C cubic
iperf3 -c 127.0.0.1 -t 2 -C bbr

Stop the server afterward.

Show Packet Capture

dumpcap -i lo -a duration:3 -w captures/demo.pcapng
wireshark captures/demo.pcapng

Clean Up at the End

sudo mn -c
deactivate

Setup complete!
