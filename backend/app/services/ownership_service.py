from datetime import datetime
from app.database.mongodb import db

async def transfer_character(owner_id:str, new_owner_id:str, character_id:str):
    result = await db.characters.update_one(
        {"_id": character_id, "owner_id": owner_id},
        {"$set":{
            "owner_id": new_owner_id,
            "updated_at": datetime.utcnow()
        }}
    )
    return {"success": result.modified_count > 0}
