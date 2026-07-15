from app.database.mongodb import db


class TradeRepository:
    async def create(self, trade: dict):
        result = await db.trades.insert_one(trade)
        trade['_id'] = str(result.inserted_id)
        return trade

    async def list_user_trades(self, user_id: str):
        result = []
        cursor = db.trades.find({'from_user': user_id})
        async for item in cursor:
            item['_id'] = str(item['_id'])
            result.append(item)
        return result


trade_repository = TradeRepository()
