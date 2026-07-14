from datetime import datetime


def create_history(user_id, action, detail):
    return {
        'user_id': user_id,
        'action': action,
        'detail': detail,
        'created_at': datetime.utcnow()
    }
