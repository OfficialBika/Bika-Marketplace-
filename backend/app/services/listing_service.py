from datetime import datetime
from app.database.mongodb import db

async def create_listing(data: dict):
    data['status'] = 'active'
    data['created_at'] = datetime.utcnow()
    result = await db.marketplace_listings.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return data

async def get_active_listings():
    return await db.marketplace_listings.find({'status':'active'}).to_list(100)
