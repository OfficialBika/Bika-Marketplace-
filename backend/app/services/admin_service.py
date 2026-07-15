from datetime import datetime

async def update_character(character_id: str, data: dict, db):
    data["updated_at"] = datetime.utcnow()
    result = await db.characters.update_one(
        {"_id": character_id},
        {"$set": data}
    )
    return {"success": result.modified_count > 0}

async def delete_character(character_id: str, db):
    result = await db.characters.delete_one({"_id": character_id})
    return {"success": result.deleted_count > 0}
