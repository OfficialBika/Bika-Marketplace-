from datetime import datetime
from app.database.mongodb import db


async def create_order(user_id: str, character_id: str, amount: float):
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
