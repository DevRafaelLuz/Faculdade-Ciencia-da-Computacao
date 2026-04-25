import hashlib, os

from aes import aes_decryption, aes_encryption, pad, unpad, xor_bytes

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)

def generate_salt() -> bytes:
    return os.urandom(16)

def generate_iv() -> bytes:
    return os.urandom(16)

# CBC

def encrypt_cbc(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    data = pad(plaintext)
    ciphertext = b''
    prev_block = iv

    for i in range(0, len(data), 16):
        block = data[i:i+16]
        block_xored = xor_bytes(block, prev_block)
        encrypted = aes_encryption(block_xored, key)
        ciphertext += encrypted
        prev_block = encrypted

    return ciphertext

def decrypt_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    plaintext = b''
    prev_block = iv

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted = aes_decryption(block, key)
        plaintext += xor_bytes(decrypted, prev_block)
        prev_block = block

    return unpad(plaintext)