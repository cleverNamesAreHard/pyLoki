import socket
import struct
import sys

def receive_icmp():
    # Create a raw socket with the ICMP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    try:
        print("Listening...")
        while True:
            # Receive packets
            pkt, addr = sock.recvfrom(1024)

            # Unpack the IP header
            ip_header = pkt[0:20]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            # Unpack the ICMP packet
            icmp_header = pkt[20:28]
            icmph = struct.unpack('!BBHHH', icmp_header)

            type, code, checksum, identifier, sequence = icmph

            # Filter to process only packets with sequence number 0xf001
            if sequence == 0xf001:
                message = pkt[28:]  # Extract the message from the packet
                print(f"Received ICMP packet from {addr[0]}: Type={type}, Code={code}, Checksum={checksum}, Identifier={identifier}, Sequence={hex(sequence)}, Message={message}")
            else:
                # Optionally print that a packet was received but not processed
                print(f"Packet received from {addr[0]} with sequence {hex(sequence)}, not processing.")
    except KeyboardInterrupt:
        print("Exiting...")
        sock.close()

if __name__ == "__main__":
    receive_icmp()






import socket
import struct
import sys

def receive_icmp():
    """
    Listens for ICMP packets and prints details of received packets that match
    specific criteria, specifically an ICMP echo request with a predefined sequence number.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    try:
        print("Listening for ICMP packets...")
        while True:
            # Receive packets
            pkt, addr = sock.recvfrom(1024)  # Buffer size of 1024 bytes

            # Unpack the IP header
            ip_header = pkt[0:20]  # IP header is the first 20 bytes
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            # Unpack the ICMP packet
            icmp_header = pkt[20:28]  # ICMP header follows IP header
            icmph = struct.unpack('!BBHHH', icmp_header)

            type, code, checksum, identifier, sequence = icmph

            # Filter to process only packets with sequence number 0xf001
            if sequence == 0xf001:
                message = pkt[28:].decode('utf-8')  # Decode the message part of the packet
                print(f"Received ICMP packet from {addr[0]}: Type={type}, Code={code}, Checksum={checksum}, Identifier={identifier}, Sequence={hex(sequence)}, Message={message}")
            else:
                # Optionally print that a packet was received but not processed
                print(f"Packet received from {addr[0]} with sequence {hex(sequence)}, not processing.")
    except KeyboardInterrupt:
        print("Exiting...")
        sock.close()

if __name__ == "__main__":
    receive_icmp()
