from datetime import datetime
from app.database.mongodb import db


async def create_purchase(user_id: str, character_id: str, amount: float):
    purchase = {
        "user_id": user_id,
        "character_id": character_id,
        "amount": amount,
        "coin": "BKC",
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    result = await db.marketplace_orders.insert_one(purchase)

    purchase["_id"] = str(result.inserted_id)

    return purchase
