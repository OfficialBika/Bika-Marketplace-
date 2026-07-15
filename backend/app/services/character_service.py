import os
from app.database.mongodb import db

async def get_featured_characters(rarity=None, limit=8):
    rarity = rarity or os.getenv("SHOW_RARITY", "Supreme")
    limit = int(limit or os.getenv("FEATURED_LIMIT", "8"))

    cursor = db.characters.find({
        "rarity": rarity,
        "status": "active"
    }).limit(limit)

    return await cursor.to_list(length=limit)
