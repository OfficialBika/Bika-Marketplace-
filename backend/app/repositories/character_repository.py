from app.database.mongodb import db


class CharacterRepository:
    async def get_by_id(self, character_id: str):
        return await db.characters.find_one({'_id': character_id})

    async def list_by_owner(self, owner_id: str):
        result = []
        cursor = db.characters.find({'owner_id': owner_id})
        async for item in cursor:
            item['_id'] = str(item['_id'])
            result.append(item)
        return result


character_repository = CharacterRepository()
