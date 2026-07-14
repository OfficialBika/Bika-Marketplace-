from datetime import datetime
from app.database.mongodb import db


async def create_auction(character_id: str, seller_id: str, start_price: float):
    auction = {
        'character_id': character_id,
        'seller_id': seller_id,
        'start_price': start_price,
        'current_bid': start_price,
        'status': 'active',
        'created_at': datetime.utcnow()
    }
    result = await db.auctions.insert_one(auction)
    auction['_id'] = str(result.inserted_id)
    return auction
