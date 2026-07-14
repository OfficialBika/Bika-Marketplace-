from datetime import datetime


def create_ledger_entry(user_id: str, amount: float, action: str):
    return {
        'user_id': user_id,
        'amount': amount,
        'action': action,
        'coin': 'BKC',
        'created_at': datetime.utcnow()
    }
