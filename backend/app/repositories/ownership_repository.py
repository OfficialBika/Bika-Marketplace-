from datetime import datetime
from app.database.mongodb import db


class OwnershipRepository:
    async def transfer(self, character_id: str, new_owner_id: str):
        result = await db.characters.update_one(
            {'_id': character_id},
            {'$set': {'owner_id': new_owner_id, 'updated_at': datetime.utcnow()}}
        )
        return result.modified_count > 0

    async def history(self, data: dict):
        data['created_at'] = datetime.utcnow()
        await db.ownership_history.insert_one(data)


ownership_repository = OwnershipRepository()
