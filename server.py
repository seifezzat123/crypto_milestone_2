
import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

HOST = "127.0.0.1"
PORT = 5000

KEY = b"12345678"

print("Legacy Bank Server")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)

    print("Waiting for client...")

    connection, address = server.accept()

    with connection:
        print("Client connected:", address)

        encrypted_message = b""

        while True:
            data = connection.recv(4096)
            if not data:
                break
            encrypted_message += data

        print("Encrypted Message (HEX):",
              encrypted_message.hex())

        if encrypted_message:
            try:
                cipher = DES.new(KEY, DES.MODE_ECB)
                padded_message = cipher.decrypt(encrypted_message)
                plaintext = unpad(
                    padded_message, DES.block_size
                )

                print("Decrypted Message:",
                      plaintext.decode("utf-8"))

            except (ValueError, UnicodeDecodeError) as error:
                print("Decryption failed:", error)
        else:
            print("No encrypted message received.")
