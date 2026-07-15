from datetime import datetime
from app.database.mongodb import db

async def create_bid(user_id:str, auction_id:str, amount:float):
    bid = {
        "user_id": user_id,
        "auction_id": auction_id,
        "amount": amount,
        "created_at": datetime.utcnow()
    }
    await db.bids.insert_one(bid)
    return bid
