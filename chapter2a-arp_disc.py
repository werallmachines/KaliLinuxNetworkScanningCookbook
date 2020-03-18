#!/usr/bin/env python3

import logging
import subprocess
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sr1,ARP

if len(sys.argv) != 2:
        print("Usage - ./arp_disc.py [interface]")
        print("Example - ./arp_disc.py eth0")
        print("Example will perform an ARP scan of the local subnet to which eth0 is assigned")
        sys.exit()

interface = str(sys.argv[1])

ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet' | cut -d ':' -f 2 | cut -d ' ' -f 10", shell=True).strip().decode('ascii')
prefix = ip.split('.')[0] + '.' + ip.split('.')[1] + '.' + ip.split('.')[2] + '.'

for addr in range(0,254):
    answer = sr1(ARP(pdst=prefix+str(addr)), timeout=2, verbose=0)
    if answer == None:
        pass
    else:
        print(prefix+str(addr))
