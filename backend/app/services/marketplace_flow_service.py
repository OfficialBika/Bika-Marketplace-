from datetime import datetime

async def complete_purchase(user_id, character_id, amount, db):
    order = {
        "user_id": user_id,
        "character_id": character_id,
        "amount": amount,
        "status": "completed",
        "created_at": datetime.utcnow()
    }
    result = await db.marketplace_orders.insert_one(order)
    return str(result.inserted_id)
