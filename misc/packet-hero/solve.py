#!/usr/bin/env python3
import re
import shutil
import subprocess
import sys
from pathlib import Path

from scapy.layers.inet import TCP
from scapy.packet import Raw
from scapy.utils import rdpcap

from pwnlib.tubes.listen import listen

pcap = rdpcap("packet-hero.pcap")
data = []
curr_dat = bytearray()
for packet in pcap:
	if Raw in packet:  # is rsync packet and not just tcp
		if packet[TCP].sport == 873:  # server sent
			curr_dat.extend(packet[Raw].load)
		elif packet[TCP].dport == 873:  # client sent
			if curr_dat:
				data.append(curr_dat)
				curr_dat = bytearray()

d = Path("out/")
if d.exists():
	shutil.rmtree(d)
d.mkdir()
(d / "files").mkdir()

s = listen(3000)
p = subprocess.Popen(
	"rsync -rzv rsync://localhost:3000/files/ out/",
	shell=True,
	stdout=sys.stdout,
	stderr=sys.stderr
)

#replay server packets
s.wait_for_connection()
for datum in data:
	s.recv()
	s.send(datum)
p.communicate()

with open("out/files/flag.txt") as f:
	print(re.search(r"flag{.*?}", f.read()).group(0))

shutil.rmtree(d)
