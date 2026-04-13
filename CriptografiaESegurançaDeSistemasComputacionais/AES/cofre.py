import sys, os, getpass

from kdf import derive_key, generate_salt, generate_iv
from cbc import encrypt_cbc, decrypt_cbc
from file_io import write_encrypted, read_encrypted

def cmd_cifrar(filepath: str):
    if not os.path.exists(filepath):
        print(f'Arquivo {filepath} não encontrado!')
        sys.exit(1)

    password = getpass.getpass("Senha: ")

    salt = generate_salt()
    iv = generate_iv()
    key = derive_key(password, salt)

    with open(filepath, 'rb') as file:
        plaintext = file.read()

    ciphertext = encrypt_cbc(plaintext, key, iv)

    output_path = filepath + '.cifrado'
    write_encrypted(output_path, salt, iv, ciphertext)

def cmd_decifrar(filepath: str):
    if not os.path.exists(filepath):
        print(f'Arquivo {filepath} não encontrado!')
        sys.exit(1)

    password = getpass.getpass("Senha: ")

    try:
        salt, iv, ciphertext = read_encrypted(filepath)
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

    key = derive_key(password, salt)

    try: 
        plaintext = decrypt_cbc(ciphertext, key, iv)
        print(plaintext.decode('utf-8'))
    except Exception:
        print("Senha incorreta ou arquivo corrompido!")
        sys.exit(1)

def main():
    command = sys.argv[1]

    if command == "cifrar" and len(sys.argv) == 3:
        cmd_cifrar(sys.argv[2])
    elif command == "decifrar" and len(sys.argv) == 3:
        cmd_decifrar(sys.argv[2])
    else:
        print("Comando incorreto ou inválido!")

if __name__ == "__main__":
    main()