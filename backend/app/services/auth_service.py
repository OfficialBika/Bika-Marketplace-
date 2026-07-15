import jwt
import os


def create_token(user_id: str):
    payload = {"user_id": user_id}
    secret = os.getenv("JWT_SECRET", "change_me")
    return jwt.encode(payload, secret, algorithm="HS256")


def verify_token(token: str):
    secret = os.getenv("JWT_SECRET", "change_me")
    return jwt.decode(token, secret, algorithms=["HS256"])
