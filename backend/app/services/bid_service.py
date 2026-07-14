from datetime import datetime
from app.database.mongodb import db


async def create_bid(auction_id: str, user_id: str, amount: float):
    bid = {
        'auction_id': auction_id,
        'user_id': user_id,
        'amount': amount,
        'status': 'active',
        'created_at': datetime.utcnow()
    }
    result = await db.bids.insert_one(bid)
    bid['_id'] = str(result.inserted_id)
    return bid
