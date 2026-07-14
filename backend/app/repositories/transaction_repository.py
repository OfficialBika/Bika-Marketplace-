from datetime import datetime
from app.database.mongodb import db


class TransactionRepository:
    async def create(self, data: dict):
        data['created_at'] = datetime.utcnow()
        result = await db.wallet_transactions.insert_one(data)
        return str(result.inserted_id)


transaction_repository = TransactionRepository()
