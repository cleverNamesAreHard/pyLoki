# pyLoki: Covert Communication Using ICMP

## Overview
pyLoki demonstrates how ICMP packets can be utilized for covert communication, inspired by the methodologies originally outlined in the Phrack magazine regarding the Loki Project. This repository contains two Python scripts: one for sending messages (`icmp_sender.py`) and another for listening to them (`icmp_listener.py`). This implementation serves as a Python-based proof of concept of the Loki Project, focusing on the use of ICMP for covert channels.

## Features
- **ICMP Utilization:** Utilizes ICMP Echo and Echo Reply packets for covert data transfers, a technique highlighted in the original Loki Project as described in Phrack.
- **No Encryption:** The current implementation does not include encryption of messages. This project is designed purely as a proof of concept. Users can extend it to include encryption for secure communications.
- **Selective Packet Identification:** Employs specialized identifiers to detect and process relevant ICMP packets efficiently, a concept directly drawn from the Loki Project's use of packet identifiers for covert communication.

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
- **Detection Techniques:** Monitoring for irregular ICMP traffic patterns can help identify the use of covert channels.
- **Prevention Strategies:** To prevent unauthorized use, consider disabling or controlling ICMP Echo traffic at your network perimeter.

## Disclaimer
This project is intended for educational and research purposes only. It is not designed for use in unauthorized or illegal activities. The creators and maintainers of pyLoki are not responsible for misuse of this software or any legal repercussions that result from such misuse. Users are advised to ensure their activities comply with local laws and regulations.

## Contributing
Contributions that enhance the project are welcome, provided they adhere to this project's guidelines.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Further Information
For those interested in detailed discussions about covert communications, refer to the original Phrack articles and the discussions in SANS Institute documentation.

## Acknowledgments
The development of this project was inspired by the original articles on the Loki Project published in Phrack magazine. Further concepts and enhancements were influenced by subsequent analyses and documentation, including works published by the SANS Institute. We extend our gratitude to all researchers and developers involved in exploring and discussing covert communication methodologies.
