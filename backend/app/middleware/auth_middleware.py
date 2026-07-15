import os
import jwt

SECRET = os.getenv("JWT_SECRET", "change-this-secret")

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except Exception:
        return None
