# 1. Implementar um modulo de backend para autenticação de usuários
#   1. Criar conta de usuário
#   2. Salvar senha criptografada em Banco de Dados
#   3. Logar usuário retornando credencial JWT
#   4. Autenticar credencial do usuário para realização de métodos sensíveis

import hashlib
import os
import base64
import hmac
import json
import time

users_db = {}

def hash_password(password: str, salt: str = None) -> str:
    if not salt:
        salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${hashed}"

SECRET_KEY = "segredo_super_secreto"

def base64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")

def create_jwt(payload: dict, secret: str = SECRET_KEY) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64url_encode(json.dumps(header).encode())
    payload_b64 = base64url_encode(json.dumps(payload).encode())
    
    signature = hmac.new(
        secret.encode(),
        f"{header_b64}.{payload_b64}".encode(),
        hashlib.sha256
    ).digest()
    signature_b64 = base64url_encode(signature)
    
    return f"{header_b64}.{payload_b64}.{signature_b64}"

def verify_jwt(token: str, secret: str = SECRET_KEY) -> dict | None:
    try:
        header_b64, payload_b64, signature_b64 = token.split(".")
        signature_check = hmac.new(
            secret.encode(),
            f"{header_b64}.{payload_b64}".encode(),
            hashlib.sha256
        ).digest()
        if base64url_encode(signature_check) != signature_b64:
            return None
        payload = json.loads(base64.urlsafe_b64decode(payload_b64 + "==").decode())
        return payload
    except Exception:
        return None
    
def protected_method(token: str):
    payload = verify_jwt(token)
    if not payload:
        return "Acesso negado!"
    if payload.get("exp") < time.time():
        return "Token expirado!"
    return "Acesso permitido ao recurso sensível."

def main():
    print("-----< Usuário Novo >-----")
    new_username = input("Digite o nome de usuário: ")
    new_password = input("Informe a Senha: ")
    users_db[new_username] = {"password": hash_password(new_password)}

    print("--------< Entrar >--------")
    username: str = input("Usuário: ")
    password: str = input("Senha: ")

    def login(username, password):
        stored = users_db.get(username)
        if not stored:
            return None
        salt, hashed = stored["password"].split("$")
        if hash_password(password, salt) == stored["password"]:
            payload = {"user": username, "exp": time.time() + 3600}
            return create_jwt(payload)
        return None

    token = login(username, password)
    print("JWT:", token)

    print(protected_method(token))

main()