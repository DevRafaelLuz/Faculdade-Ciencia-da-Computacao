import hashlib, os

def derive_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)

def generate_salt() -> bytes:
    return os.urandom(16)

def generate_iv() -> bytes:
    return os.urandom(16)