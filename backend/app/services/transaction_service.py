from app.repositories.transaction_repository import transaction_repository


class TransactionService:
    async def create_purchase(self, buyer_id: str, seller_id: str, character_id: str, amount: float):
        transaction = {
            'type': 'purchase',
            'buyer_id': buyer_id,
            'seller_id': seller_id,
            'character_id': character_id,
            'amount': amount,
            'coin': 'BKC'
        }

        return await transaction_repository.create(transaction)


transaction_service = TransactionService()
