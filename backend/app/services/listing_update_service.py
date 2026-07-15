from datetime import datetime

async def update_listing(listing_id: str, data: dict, db):
    data["updated_at"] = datetime.utcnow()
    result = await db.marketplace_listings.update_one(
        {"_id": listing_id},
        {"$set": data}
    )
    return {"success": result.modified_count > 0}
