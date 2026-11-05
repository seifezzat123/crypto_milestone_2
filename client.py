
import socket
from des import encrypt_ecb

HOST = "127.0.0.1"
PORT = 5000

KEY = b"12345678"

print("Legacy Bank Client")

message = input("Enter your transaction message: ")

plaintext = message.encode("utf-8")

encrypted_message = encrypt_ecb(plaintext, KEY)

print("\nOriginal Message:", message)
print("Encrypted Message (HEX):", encrypted_message.hex())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall(encrypted_message)

print("\nEncrypted message sent successfully!")
