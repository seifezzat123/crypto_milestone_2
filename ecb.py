from des import encrypt_ecb

KEY = b"legacy26"

message = b"5000 EUR5000 EUR"

encrypted = encrypt_ecb(message, KEY)

plaintext_blocks = [
    message[i:i + 8]
    for i in range(0, len(message), 8)
]

ciphertext_blocks = [
    encrypted[i:i + 8]
    for i in range(0, len(encrypted), 8)
]

print("\nExpected ECB Behaviour")
print(f"{'Plaintext':<25} {'Ciphertext'}")


for i in range(len(plaintext_blocks)):
    plaintext = plaintext_blocks[i].decode()
    ciphertext = ciphertext_blocks[i].hex().upper()

    print(f"{plaintext:<25} Block {i + 1}: {ciphertext}")


if ciphertext_blocks[0] == ciphertext_blocks[1]:
    print("Block 1 ciphertext = Block 2 ciphertext")
else:
    print("The ciphertext blocks are different.")

