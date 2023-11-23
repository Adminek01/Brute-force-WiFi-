import itertools
from scapy.all import *

def generate_passwords(characters, length):
    return [''.join(p) for p in itertools.product(characters, repeat=length)]

def try_credentials(username, password, target_ip, target_port):
    # W tym miejscu można dodać logikę próby uwierzytelnienia na urządzeniu sieciowym.
    # Na potrzeby przykładu, używamy funkcji print, co jest niebezpieczne i niezalecane w rzeczywistych testach.

    print(f"Trying {username}:{password} on {target_ip}:{target_port}")

def main():
    target_ip = input("Podaj IP: ")
    target_port = input("Podaj Port: ")
    username = "admin"
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password_length = 8

    passwords = generate_passwords(character_set, password_length)

    for password in passwords:
        try_credentials(username, password, target_ip, target_port)

if __name__ == "__main__":
    main()
