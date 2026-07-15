import hashlib
import os

def hash_value(value: str):
    secret = os.getenv("SECURITY_SECRET", "change-secret")
    return hashlib.sha256((secret + value).encode()).hexdigest()
