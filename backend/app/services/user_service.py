from datetime import datetime
from app.database.mongodb import db

async def create_or_update_user(data: dict):
    user = {
        "telegram_id": str(data.get("id")),
        "username": data.get("username"),
        "updated_at": datetime.utcnow()
    }

    await db.users.update_one(
        {"telegram_id": user["telegram_id"]},
        {"$set": user},
        upsert=True
    )

    return user
