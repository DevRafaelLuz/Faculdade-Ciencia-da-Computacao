from aes import aes_decryption, aes_encryption

NIST_VECTORS = [
    {
        "description": "NIST FIPS 197 — AES-128",
        "key":      bytes.fromhex("000102030405060708090a0b0c0d0e0f"),
        "plaintext":  bytes.fromhex("00112233445566778899aabbccddeeff"),
        "expected":   bytes.fromhex("69c4e0d86a7b04300d8a8eea56031a89"),
    },
    {
        "description": "NIST FIPS 197 — AES-256",
        "key":      bytes.fromhex("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"),
        "plaintext":  bytes.fromhex("00112233445566778899aabbccddeeff"),
        "expected":   bytes.fromhex("8ea2b7ca516745bfeafc49904b496089"),
    },
]

def run_tests():
    all_ok = True

    for i in NIST_VECTORS:
        result = aes_encryption(i['plaintext'], i['key'])

        if result == i['expected']:
            print(f'[SUCESSO] {i['description']}')
        else:
            print(f'[FALHA] {i['description']}')
            print(f'esperado: {i['expected'].hex()}')
            print(f'obtido: {result.hex()}')
            all_ok = False
    
    key = bytes.fromhex('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f')
    original = b'Teste de roundtrip!'
    encrypted = aes_encryption(original, key)

    if len(original) == 16:
        decrypted = aes_decryption(encrypted, key)

        if decrypted == original:
            print('[SUCESSO] Roundtrip AES-256 (cifra + decifra)')
        else:
            print("[FALHA]   Roundtrip AES-256")
            all_ok = False

    return all_ok