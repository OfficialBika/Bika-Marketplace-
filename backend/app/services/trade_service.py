from datetime import datetime
from app.database.mongodb import db


async def create_trade(from_user: str, to_user: str, character_id: str):
    trade = {
        'from_user': from_user,
        'to_user': to_user,
        'character_id': character_id,
        'status': 'pending',
        'created_at': datetime.utcnow()
    }
    result = await db.trades.insert_one(trade)
    trade['_id'] = str(result.inserted_id)
    return trade
