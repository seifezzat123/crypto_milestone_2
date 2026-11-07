IP = [
    58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,
]

IP_INV = [
    40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
    38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
    36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
    34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25,
]

E = [
    32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,
    12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,
    22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1,
]

P = [
    16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
    2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25,
]

PC1 = [
    57,49,41,33,25,17,9,1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,21,13,5,28,20,12,4,
]

PC2 = [
    14,17,11,24,1,5,3,28,15,6,21,10,
    23,19,12,4,26,8,16,7,27,20,13,2,
    41,52,31,37,47,55,30,40,51,45,33,48,
    44,49,39,56,34,53,46,42,50,36,29,32,
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

SBOX = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12],
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14],
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3],
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13],
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12],
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11],
    ],
]

BLOCK_SIZE = 8


def bits(value, width):
    return f"{value:0{width}b}"


def permute(value, input_width, table):
    """Read 1-indexed bit positions, with position 1 the most significant bit."""
    output = 0
    for position in table:
        output = (output << 1) | ((value >> (input_width - position)) & 1)
    return output


def rotate_left_28(value, amount):
    return ((value << amount) | (value >> (28 - amount))) & ((1 << 28) - 1)


def generate_round_keys(key):
    """Return the 16 48-bit DES subkeys for an 8-byte key."""
    if not isinstance(key, bytes) or len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes")

    key64 = int.from_bytes(key, "big")
    key56 = permute(key64, 64, PC1)
    c, d = key56 >> 28, key56 & ((1 << 28) - 1)

    round_keys = []

    for amount in SHIFTS:
        c, d = rotate_left_28(c, amount), rotate_left_28(d, amount)
        round_keys.append(permute((c << 28) | d, 56, PC2))

    return round_keys


def des_round(left, right, round_key, show_steps=False):
    """One complete Feistel round; inputs/outputs are two 32-bit halves."""
    if not (0 <= left < 2**32 and 0 <= right < 2**32 and 0 <= round_key < 2**48):
        raise ValueError("Invalid DES round input")

    expanded = permute(right, 32, E)
    mixed = expanded ^ round_key
    substituted = 0
    lookups = []

    for index in range(8):
        six = (mixed >> (42 - 6 * index)) & 0b111111
        row = ((six >> 5) << 1) | (six & 1)
        column = (six >> 1) & 0b1111
        result = SBOX[index][row][column]

        substituted = (substituted << 4) | result
        lookups.append((index + 1, six, row, column, result))

    p_output = permute(substituted, 32, P)
    new_left, new_right = right, left ^ p_output

    if show_steps:
        print("L0:              ", bits(left, 32))
        print("R0:              ", bits(right, 32))
        print("K1:              ", bits(round_key, 48))
        print("E(R0):           ", bits(expanded, 48))
        print("E(R0) XOR K1:    ", bits(mixed, 48))

        for number, six, row, column, result in lookups:
            print(
                f"S{number}: {bits(six, 6)}  row={bits(row, 2)} ({row}) "
                f"col={bits(column, 4)} ({column}) -> {result} ({bits(result, 4)})"
            )

        print("S-box output:    ", bits(substituted, 32))
        print("P output:        ", bits(p_output, 32))
        print("L1 = R0:         ", bits(new_left, 32))
        print("R1 = L0 XOR P:   ", bits(new_right, 32))
        print("Round 1 output:  ", bits((new_left << 32) | new_right, 64))

    return new_left, new_right


def process_block(block, round_keys, show_first_round=False):
    """Encrypt/decrypt exactly one 8-byte block using the given key order."""
    if len(block) != BLOCK_SIZE:
        raise ValueError("DES block must be exactly 8 bytes")

    input64 = int.from_bytes(block, "big")
    initial = permute(input64, 64, IP)
    left, right = initial >> 32, initial & 0xFFFFFFFF

    if show_first_round:
        print("Input block:     ", bits(input64, 64))
        print("After IP:        ", bits(initial, 64))

    for index, subkey in enumerate(round_keys):
        left, right = des_round(
            left, right, subkey,
            show_steps=show_first_round and index == 0
        )

    preoutput = (right << 32) | left
    output64 = permute(preoutput, 64, IP_INV)

    return output64.to_bytes(8, "big")


def encrypt_ecb(plaintext, key, show_first_round=False):
    """Encrypt any bytes using DES-ECB with PKCS#7 padding."""
    if not isinstance(plaintext, bytes):
        raise TypeError("Plaintext must be bytes")

    padding_length = BLOCK_SIZE - len(plaintext) % BLOCK_SIZE
    padded = plaintext + bytes([padding_length]) * padding_length

    keys = generate_round_keys(key)

    return b"".join(
        process_block(
            padded[i:i + BLOCK_SIZE],
            keys,
            show_first_round=show_first_round and i == 0
        )
        for i in range(0, len(padded), BLOCK_SIZE)
    )


def decrypt_ecb(ciphertext, key):
    """Decrypt DES-ECB bytes and validate/remove PKCS#7 padding."""
    if not isinstance(ciphertext, bytes) or not ciphertext or len(ciphertext) % BLOCK_SIZE:
        raise ValueError("Ciphertext must contain complete 8-byte blocks")

    keys = generate_round_keys(key)[::-1]

    padded = b"".join(
        process_block(ciphertext[i:i + BLOCK_SIZE], keys)
        for i in range(0, len(ciphertext), BLOCK_SIZE)
    )

    amount = padded[-1]

    if amount < 1 or amount > BLOCK_SIZE or padded[-amount:] != bytes([amount]) * amount:
        raise ValueError("Invalid padding (wrong key or corrupted ciphertext)")

    return padded[:-amount]

