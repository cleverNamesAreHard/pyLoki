# pyLoki: Communication Using ICMP

## Overview
pyLoki demonstrates how ICMP packets can be utilized for communication. This repository contains two Python scripts: one for sending messages (`icmp_sender.py`) and another for listening to them (`icmp_listener.py`). This is a Python-based implementation of the Loki Project as a proof of concept.

## Features
- **ICMP Utilization:** Utilizes ICMP Echo and Echo Reply packets for covert data transfers.
- **No Encryption:** The current implementation does not include encryption of messages. This is designed purely as a proof of concept, and so encryption is not needed.
- **Selective Packet Identification:** Employs specialized identifiers to detect and process relevant ICMP packets efficiently.

## Installation
Clone the repository with the following command:
```bash
git clone https://github.com/cleverNamesAreHard/pyLoki.git
```

## Usage
Ensure Python 3.x is installed on your machine before proceeding.

### Running the Listener
To operate the listener script, execute:
```bash
sudo python icmp_listener.py
```
Note: Administrative privileges may be required, especially on systems like WSL in Windows.

### Sending Messages
To dispatch a message, use the following command:
```bash
sudo python icmp_sender.py <destination_ip> "Your secret message here"
```
Note: Sending messages may also necessitate administrative privileges depending on your system’s setup.

## Detection and Mitigation
- **Detection Techniques:** Monitoring for irregular ICMP traffic patterns can help identify the use of unauthorized communication channels.
- **Prevention Strategies:** To prevent unauthorized use, consider disabling or controlling ICMP Echo traffic at your network perimeter.

## Disclaimer
This project is intended for educational and research purposes only. It is not designed for use in unauthorized or illegal activities. The creators and maintainers of pyLoki are not responsible for misuse of this software or any legal repercussions that result from such misuse. Users are advised to ensure their activities comply with local laws and regulations.

## Acknowledgments
The development of this project was inspired by the Loki Project. We thank the original creators for their pioneering work in network security.

Please see Phrack volumes 49 (whitepaper) and 51 (LOKI2 implementation) for the reference for this repo.

Further resources:
* James P. Goltz, "Under the Radar: A Look at Three Covert Communications Channels," SANS Institute, January 2003, accessed April 21, 2024, https://www.giac.org/paper/gsec/2601/radar-covert-communications-channels/104464.

