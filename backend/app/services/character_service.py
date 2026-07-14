from app.database.mongodb import db

async def get_character(character_id: str):
    return await db.characters.find_one({"_id": character_id})

async def get_user_characters(user_id: str):
    return await db.characters.find({"owner_id": user_id}).to_list(100)
