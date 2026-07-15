import hashlib
import os


def hash_value(value: str):
    return hashlib.sha256(value.encode()).hexdigest()


def get_secret():
    return os.getenv('JWT_SECRET', 'change_me')
