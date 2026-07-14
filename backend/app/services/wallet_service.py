from app.repositories.wallet_repository import wallet_repository


class WalletService:
    async def get_wallet(self, user_id: str):
        transactions = await wallet_repository.get_transactions(user_id)
        balance = 0

        for tx in reversed(transactions):
            tx_type = tx.get('type') or tx.get('action')
            amount = tx.get('amount', 0)

            if tx_type in ['credit', 'reward', 'deposit']:
                balance += amount
            elif tx_type in ['debit', 'purchase', 'withdraw']:
                balance -= amount

        return {
            'user_id': user_id,
            'coin': 'BKC',
            'balance': balance,
            'transactions': transactions
        }


wallet_service = WalletService()


async def get_wallet(user_id: str):
    return await wallet_service.get_wallet(user_id)
