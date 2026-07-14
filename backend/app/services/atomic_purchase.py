from datetime import datetime
from app.database.mongodb import db
from app.core.errors import TransactionError


async def purchase_character(user_id: str, character_id: str, amount: float):
    if amount <= 0:
        raise TransactionError('Invalid purchase amount')

    order = {
        'user_id': user_id,
        'character_id': character_id,
        'amount': amount,
        'coin': 'BKC',
        'status': 'pending',
        'created_at': datetime.utcnow()
    }

    result = await db.marketplace_orders.insert_one(order)
    order['_id'] = str(result.inserted_id)
    return order
