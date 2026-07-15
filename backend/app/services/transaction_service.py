from datetime import datetime
from app.database.mongodb import db

async def create_transaction(user_id:str, tx_type:str, amount:float, reference=None):
    data = {
        "user_id": user_id,
        "type": tx_type,
        "amount": amount,
        "reference": reference,
        "created_at": datetime.utcnow()
    }
    result = await db.wallet_transactions.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return data
