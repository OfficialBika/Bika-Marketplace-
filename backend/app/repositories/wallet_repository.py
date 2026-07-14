from app.database.mongodb import db


class WalletRepository:
    async def get_transactions(self, user_id: str):
        items = []
        cursor = db.wallet_transactions.find({'user_id': user_id}).sort('created_at', -1)
        async for item in cursor:
            item['_id'] = str(item['_id'])
            items.append(item)
        return items


wallet_repository = WalletRepository()
