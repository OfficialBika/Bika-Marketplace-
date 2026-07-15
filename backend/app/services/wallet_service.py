from app.database.mongodb import db

async def get_balance(user_id:str):
    wallet = await db.wallets.find_one({"user_id": user_id})
    return wallet or {
        "user_id": user_id,
        "balance": 0,
        "currency": "BKC"
    }
