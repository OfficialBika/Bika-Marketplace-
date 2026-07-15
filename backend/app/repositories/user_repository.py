from app.database.mongodb import db


class UserRepository:
    async def get_by_id(self, user_id: str):
        return await db.users.find_one({'id': user_id})

    async def save(self, user: dict):
        await db.users.update_one(
            {'id': user.get('id')},
            {'$set': user},
            upsert=True
        )
        return user


user_repository = UserRepository()
