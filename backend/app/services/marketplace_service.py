from app.repositories.marketplace_repository import marketplace_repository


class MarketplaceService:
    async def get_items(self, limit: int = 20, rarity: str = None):
        return await marketplace_repository.list_items(limit, rarity)


marketplace_service = MarketplaceService()
