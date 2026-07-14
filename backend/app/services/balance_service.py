from app.database.mongodb import db


class BalanceService:
    async def get_balance(self, user_id: str):
        balance = 0
        cursor = db.wallet_transactions.find({'user_id': user_id})

        async for tx in cursor:
            amount = tx.get('amount', 0)
            if tx.get('type') in ['credit', 'reward', 'deposit']:
                balance += amount
            elif tx.get('type') in ['debit', 'purchase', 'withdraw']:
                balance -= amount

        return balance

    async def can_spend(self, user_id: str, amount: float):
        return await self.get_balance(user_id) >= amount


balance_service = BalanceService()
