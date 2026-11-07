import socket
from des import encrypt_ecb

HOST = "127.0.0.1"
PORT = 5000

KEY = b"legacy26"

print("Legacy Bank Client")

message = input("Enter your transaction message: ")

plaintext = message.encode("utf-8")

# Encrypt the message and display the first Feistel round results
encrypted_message = encrypt_ecb(
    plaintext, KEY, show_first_round=True
)

print("\nOriginal Message:", message)
print("Encrypted Message (HEX):", encrypted_message.hex())
print(
    "Encrypted Message (Binary):",
    ''.join(format(byte, '08b') for byte in encrypted_message)
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    client.sendall(encrypted_message)

print("\nEncrypted message sent successfully!")
