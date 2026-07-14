import os
from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = os.getenv('JWT_SECRET', 'change-this-secret')
ALGORITHM = 'HS256'


def create_token(user_id: str):
    payload = {
        'sub': user_id,
        'exp': datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
