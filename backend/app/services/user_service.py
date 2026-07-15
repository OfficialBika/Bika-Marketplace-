from app.models.user import User
from app.database.mongodb import db


async def get_user(user_id: str):
    user = await db.users.find_one({"id": user_id})
    return user or User(id=user_id)


async def update_user(user_id: str, data: dict):
    await db.users.update_one(
        {"id": user_id},
        {"$set": data},
        upsert=True
    )
    return {
        'user_id': user_id,
        'updated': data
    }
