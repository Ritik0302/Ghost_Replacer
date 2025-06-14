# SpoofStrike
# 🕵️‍♂️ SilentLink - ARP Spoofing Tool

A lightweight Python-based **ARP Spoofing** script built using **Scapy**. This tool enables Man-in-the-Middle (MITM) attacks by poisoning ARP caches of a target and a router on a local network.

> ⚠️ For educational and ethical hacking purposes only.

---

## 🔧 Features

- Real-time ARP spoofing between victim and gateway
- Continuous MITM position maintenance
- ARP table restoration on script termination
- Clean CLI interface

---

## 📦 Requirements

- Python 3.x
- Scapy

Install dependencies:
```bash
pip install scapy
```

## 🚀 Usage

```bash
sudo python3 arp_spoofer.py
```
## ⚙️ How It Works

Sends spoofed ARP replies to both victim and router
Associates your MAC with the gateway and vice versa
Puts you in a Man-in-the-Middle position
Restores original ARP tables on exit using real MAC addresses

## 👨‍💻 Author
Developed by Ritik Singhania

## ⚠️ Disclaimer
This tool is intended for educational and authorized penetration testing use only.
Do not use on any network without explicit permission.
The developer holds no responsibility for any illegal or unethical use of this script.
