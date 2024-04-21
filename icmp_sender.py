import socket
import struct
import sys

def checksum(source_string):
    """
    Calculate the Internet Checksum of the supplied data. The checksum algorithm is
    simple, using a 32 bit accumulator (sum), we add sequential 16 bit words to it, and
    at the end, fold back all the carry bits from the top 16 bits into the lower 16 bits.
    """
    sum = 0
    count_to = (len(source_string) // 2) * 2
    count = 0
    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff  # Necessary to ensure sum stays within 32-bit bounds
        count += 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff  # Add the last byte if the length is odd

    sum = (sum >> 16) + (sum & 0xffff)
    sum += sum >> 16
    answer = ~sum
    answer = answer & 0xffff
    # Swap bytes
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def create_packet(id, message):
    """
    Creates an ICMP echo request packet with a fixed identifier and sequence number.
    The packet includes a user-defined message encoded as bytes.
    """
    header = struct.pack('!BBHHH', 8, 0, 0, id, 0xf001)  # Type 8 (Echo), Code 0
    data = message.encode()  # Encode the message to bytes
    # Calculate the checksum on the data and the dummy header
    my_checksum = checksum(header + data)
    # Now that we have the right checksum, we pack the header again with the correct checksum
    header = struct.pack('!BBHHH', 8, 0, socket.htons(my_checksum), id, 0xf001)
    packet = header + data
    return packet

def send_one_ping(dest_addr, id, message):
    """
    Sends a single ICMP packet to the specified destination address.
    This requires root privileges due to the use of raw sockets.
    """
    icmp = socket.getprotobyname('icmp')
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    except PermissionError:
        e = sys.exc_info()[1]
        print("Operation not permitted: ICMP messages can only be sent from processes running as root.")
        return
    except Exception as e:
        print("Exception: %s" % (e))
        return

    packet = create_packet(id, message)
    sock.sendto(packet, (dest_addr, 1))
    sock.close()

if __name__ == '__main__':
    dest = sys.argv[1]
    message = " ".join(sys.argv[2:])  # Join all remaining arguments to form the message
    send_one_ping(dest, 1, message)  # id is arbitrarily set to 1
