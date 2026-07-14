from app.database.mongodb import db


class MarketplaceRepository:
    async def list_items(self, limit: int = 20):
        items = []
        cursor = db.marketplace_listings.find({}).limit(limit)
        async for item in cursor:
            item['_id'] = str(item['_id'])
            items.append(item)
        return items


marketplace_repository = MarketplaceRepository()
