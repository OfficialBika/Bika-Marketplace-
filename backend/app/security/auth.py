from datetime import datetime, timedelta
import os

JWT_SECRET = os.getenv('JWT_SECRET','change_me')


def create_session(user_id: str):
    return {
        'user_id': user_id,
        'expires_at': datetime.utcnow() + timedelta(days=7)
    }


def verify_user(user_id: str):
    return bool(user_id)
