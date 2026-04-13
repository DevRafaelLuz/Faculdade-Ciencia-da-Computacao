import hashlib

s_box_string = '63 7c 77 7b f2 6b 6f c5 30 01 67 2b fe d7 ab 76' \
            'ca 82 c9 7d fa 59 47 f0 ad d4 a2 af 9c a4 72 c0' \
            'b7 fd 93 26 36 3f f7 cc 34 a5 e5 f1 71 d8 31 15' \
            '04 c7 23 c3 18 96 05 9a 07 12 80 e2 eb 27 b2 75' \
            '09 83 2c 1a 1b 6e 5a a0 52 3b d6 b3 29 e3 2f 84' \
            '53 d1 00 ed 20 fc b1 5b 6a cb be 39 4a 4c 58 cf' \
            'd0 ef aa fb 43 4d 33 85 45 f9 02 7f 50 3c 9f a8' \
            '51 a3 40 8f 92 9d 38 f5 bc b6 da 21 10 ff f3 d2' \
            'cd 0c 13 ec 5f 97 44 17 c4 a7 7e 3d 64 5d 19 73' \
            '60 81 4f dc 22 2a 90 88 46 ee b8 14 de 5e 0b db' \
            'e0 32 3a 0a 49 06 24 5c c2 d3 ac 62 91 95 e4 79' \
            'e7 c8 37 6d 8d d5 4e a9 6c 56 f4 ea 65 7a ae 08' \
            'ba 78 25 2e 1c a6 b4 c6 e8 dd 74 1f 4b bd 8b 8a' \
            '70 3e b5 66 48 03 f6 0e 61 35 57 b9 86 c1 1d 9e' \
            'e1 f8 98 11 69 d9 8e 94 9b 1e 87 e9 ce 55 28 df' \
            '8c a1 89 0d bf e6 42 68 41 99 2d 0f b0 54 bb 16'.replace(" ", "")

s_box = bytearray.fromhex(s_box_string)

rs_box = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

def state_from_bytes(data: bytes) -> [[int]]: # type: ignore
    state = [data[i*4:(i+1)*4] for i in range(len(data) // 4)]
    return state

def rot_word(word: int) -> [int]: # type: ignore
    return word[1:] + word[:1]

def sub_word(word: [int]) -> bytes: # type: ignore
    subsituted_word = bytes(s_box[i] for i in word)
    return subsituted_word

def rcon(i: int) -> bytes:
    rcon_lookup = bytearray.fromhex('01020408102040801836')
    rcon_value = bytes([rcon_lookup[i-1], 0, 0, 0])
    return rcon_value

def xor_bytes(a: bytes, b: bytes):
    return bytes([x ^ y for (x, y) in zip(a, b)])

def key_expansion(key: bytes, nb: int = 4) -> [[[int]]]: # type: ignore
    nk = len(key) // 4

    key_bit_length = len(key) * 8

    if key_bit_length == 128:
        nr = 10
    elif key_bit_length == 192:
        nr = 12
    else:
        nr = 14

    w = state_from_bytes(key)

    for i in range(nk, nb * (nr + 1)):
        temp = w[i-1]

        if i % nk == 0:
            temp = xor_bytes(sub_word(rot_word(temp)), rcon(i // nk))
        elif nk > 6 and i % nk == 4:
            temp = sub_word(temp)

        w.append(xor_bytes(w[i-nk], temp))
    return [w[i*4:(i+1)*4] for i in range(len(w) // 4)]

def add_round_key(state: [[int]], key_schedule: [[[int]]], round: int): # type: ignore
    round_key = key_schedule[round]
    for r in range(len(state)):
        state[r] = [state[r][c] ^ round_key[r][c] for c in range(len(state[0]))]

def sub_bytes(state: [[int]]): # type: ignore
    for r in range(len(state)):
        state[r] = [s_box[state[r][c]] for c in range(len(state[0]))]

def shift_rows(state: [[int]]): # type: ignore
    state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
    state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
    state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]

def xtime(a: int) -> int:
    if a & 0x80:
        return ((a << 1) ^ 0x1b) & 0xff
    return a << 1

def mix_column(col: [int]): # type: ignore
    c = col[:]
    col[0] = mul(c[0], 0x02) ^ mul(c[1], 0x03) ^ c[2] ^ c[3]
    col[1] = c[0] ^ mul(c[1], 0x02) ^ mul(c[2], 0x03) ^ c[3]
    col[2] = c[0] ^ c[1] ^ mul(c[2], 0x02) ^ mul(c[3], 0x03)
    col[3] = mul(c[0], 0x03) ^ c[1] ^ c[2] ^ mul(c[3], 0x02)

def mix_columns(state: [[int]]): # type: ignore
    for r in state:
        mix_column(r)

def bytes_from_state(state: [[int]]) -> bytes: # type: ignore
    cipher = bytes(state[0] + state[1] + state[2] + state[3])
    return cipher

def aes_encryption(data: bytes, key: bytes) -> bytes:
    state = state_from_bytes(data)

    key_schedule = key_expansion(key)

    add_round_key(state, key_schedule, round=0)

    key_bit_length = len(key) * 8

    if key_bit_length == 128:
        nr = 10
    elif key_bit_length == 192:
        nr = 12
    else:
        nr = 14

    for round in range(1, nr):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, key_schedule, round)

    sub_bytes(state)
    shift_rows(state)
    add_round_key(state, key_schedule, round=nr)

    cipher = bytes_from_state(state)
    return cipher

def pad(data: bytes) -> bytes:
    padding_len = 16 - (len(data) % 16)
    return data + bytes([padding_len] * padding_len)

def unpad(data: bytes) -> bytes:
    padding_len = data[-1]
    return data[:-padding_len]

# def get_aes_key(password: str) -> bytes:
#     return hashlib.sha256(password.encode()).digest()

# def encode_credentials(text: str, password: str) -> str:
#     key = get_aes_key(password)
#     data = pad(text.encode('utf-8'))
#     ciphertext = bytearray()
    
#     for i in range(0, len(data), 16):
#         block = data[i:i+16]
#         cipher_block = aes_encryption(block, key) 
#         ciphertext.extend(cipher_block)
        
#     return ciphertext.hex()

def inv_sub_bytes(state):
    for r in range(len(state)):
        state[r] = [rs_box[state[r][c]] for c in range(len(state[0]))]

def inv_shift_rows(state):
    state[0][1], state[1][1], state[2][1], state[3][1] = \
        state[3][1], state[0][1], state[1][1], state[2][1]
    
    state[0][2], state[1][2], state[2][2], state[3][2] = \
        state[2][2], state[3][2], state[0][2], state[1][2]
    
    state[0][3], state[1][3], state[2][3], state[3][3] = \
        state[1][3], state[2][3], state[3][3], state[0][3]
    
def mul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p & 0xff

def inv_mix_column(col):
    c0, c1, c2, c3 = col
    col[0] = mul(c0, 0x0e) ^ mul(c1, 0x0b) ^ mul(c2, 0x0d) ^ mul(c3, 0x09)
    col[1] = mul(c0, 0x09) ^ mul(c1, 0x0e) ^ mul(c2, 0x0b) ^ mul(c3, 0x0d)
    col[2] = mul(c0, 0x0d) ^ mul(c1, 0x09) ^ mul(c2, 0x0e) ^ mul(c3, 0x0b)
    col[3] = mul(c0, 0x0b) ^ mul(c1, 0x0d) ^ mul(c2, 0x09) ^ mul(c3, 0x0e)

def inv_mix_columns(state):
    for r in state:
        inv_mix_column(r)

def aes_decryption(ciphertext: bytes, key: bytes) -> bytes:
    state = state_from_bytes(ciphertext)
    key_schedule = key_expansion(key)
    
    nr = 14 

    add_round_key(state, key_schedule, round=nr)
    inv_shift_rows(state)
    inv_sub_bytes(state)

    for round in range(nr - 1, 0, -1):
        add_round_key(state, key_schedule, round)
        inv_mix_columns(state)
        inv_shift_rows(state)
        inv_sub_bytes(state)

    add_round_key(state, key_schedule, round=0)

    return bytes_from_state(state)

# def decode_text(hex_cipher: str, password: str) -> str:
#     key = get_aes_key(password)
#     ciphertext = bytes.fromhex(hex_cipher)
#     plaintext_bytes = bytearray()
    
#     for i in range(0, len(ciphertext), 16):
#         block = ciphertext[i:i+16]
#         decrypted_block = aes_decryption(block, key)
#         plaintext_bytes.extend(decrypted_block)
        
#     return unpad(plaintext_bytes).decode('UTF-8')

# def main():
#     while True:
#         option = input("1. Criptografar\n2. Descriptografar\n3. Sair\nEscolha uma opção: ")
    
#         if option == '1':
#             text = input("Digite o texto: ")
#             password = input("Senha: ")
#             encrypted = encode_credentials(text, password)
#             print(f"Resultado (Hex): {encrypted}")
#         elif option == '2':
#             hex_data = input("Cole o código Hex: ")
#             password = input("Senha: ")
#             try:
#                 decrypted = decode_text(hex_data, password)

#                 if decrypted:
#                     print(f"Texto original: {decrypted}")
#                 else:
#                     print("Senha incorreta ou dados corrompidos.")
#             except Exception:
#                 print("Erro: Senha incorreta ou dados corrompidos.")
#         elif option == '3':
#             break
#         else:
#             print("Opção inválida!")

# if __name__ == "__main__":
#     main()