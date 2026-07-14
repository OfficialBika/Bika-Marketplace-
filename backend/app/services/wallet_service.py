from datetime import datetime
from app.database.mongodb import db


async def get_wallet(user_id: str):
    wallet = await db.wallet_transactions.find_one({'user_id': user_id})
    return wallet or {
        'user_id': user_id,
        'balance': 0,
        'coin': 'BKC'
    }


async def add_transaction(user_id: str, amount: float, action: str):
    return await db.wallet_transactions.insert_one({
        'user_id': user_id,
        'amount': amount,
        'action': action,
        'coin': 'BKC',
        'created_at': datetime.utcnow()
    })
