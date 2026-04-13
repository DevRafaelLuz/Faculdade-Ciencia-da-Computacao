def write_encrypted(output_path: str, salt: bytes, iv: bytes, ciphertext: bytes):
    with open(output_path, 'wb') as file:
        file.write(salt + iv + ciphertext)

def read_encrypted(input_path: str) -> tuple:
    with open(input_path, 'rb') as file:
        data = file.read()

    if len(data) < 32:
        raise ValueError("Arquivo corrompido ou inválido!")
    
    salt = data [:16]
    iv = data[16:32]
    ciphertext = data[32:]

    return salt, iv, ciphertext