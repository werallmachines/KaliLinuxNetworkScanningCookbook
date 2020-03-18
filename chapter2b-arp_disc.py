#!/usr/bin/env python3

import scapy
import logging
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sr1,ARP

if len(sys.argv) != 2:
    print("Usage - ./arp_disc.py [filename]")
    print("Example - ./arp_disc.py iplist.txt")
    print("Example will perform an ARP scan of the IP addresses listed in iplist.txt")
    sys.exit()

filename = str(sys.argv[1])
file = open(filename, 'r')

for addr in file:
    answer = sr1(ARP(pdst=addr.strip()), timeout=2, verbose=0)
    if answer == None:
        pass
    else:
        print(addr.strip())
