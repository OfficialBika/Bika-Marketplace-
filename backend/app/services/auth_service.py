import os
import jwt
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET", "change-me")

def create_token(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")
