# Wifi-Scanner
A multithread tool to scan for available APs and display their Signal Strength, Security Protocol, SSID and channels. Written in Python (Scapy Module)

# Demo

![Wifi-Scanner](demo.gif)

# Usage

Make sure you enable the monitor mode in your interface
```sudo ifconfig wlan0 down```
```sudo iwconfig wlan0 mode monitor```
```sudo ifconfig wlan0 up```

Run the script
```sudo python3 wifi_scanner.py```
