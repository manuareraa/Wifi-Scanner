from scapy.all import *
from threading import Thread
import pandas
import time
import os

#initializing an array to store the data
access_points = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Security"])

#For the entire dataset, we fix the BSSID column as the index as they are unique
access_points.set_index("BSSID", inplace=True)

#extracting all the data from the packet
def data_extraction(packet):
    
    #checking if it is a beacon frame
    if packet.haslayer(Dot11Beacon):
        
        #extracting MAC
        bssid = packet[Dot11].addr2
        
        #extracting SSID and decoding from Hex to Human Readable format
        ssid = packet[Dot11Elt].info.decode()
        
        #extracting signal strength
        try:
            dBm_Signal = packet.dBm_AntSignal
        except:
            dBm_Signal = "N/A"
        
        #extracting stats, channel and security details
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        security = stats.get("crypto")
        
        #storing the obtained data into an dataframe
        access_points.loc[bssid] = (ssid, dBm_Signal, channel, security)

#a function to print all data        
def print():
    while True:
        os.system("clear")
        print(access_points)
        time.sleep(0.5)
        
#function to change channel
def channel_change():
    channel = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        ch = ch % 14 + 1
        time.sleep(0.5)

#main thread        
if __name__ == "__main__":
    # interface name, check using iwconfig
    interface = "wlan0mon"
    
    # start the thread that prints all the networks
    printer = Thread(target=print)
    printer.daemon = True
    printer.start()
    
    # start the channel changer
    channel_changer = Thread(target=channel_change)
    channel_changer.daemon = True
    channel_changer.start()
    
    # start sniffing
    sniff(prn=data_extraction, iface=interface)
    
