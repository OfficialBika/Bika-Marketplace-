from app.repositories.marketplace_repository import marketplace_repository


class MarketplaceService:
    async def get_items(self, limit: int = 20):
        return await marketplace_repository.list_items(limit)


marketplace_service = MarketplaceService()
