from app.database.mongodb import db


class AtomicPurchaseService:
    async def purchase(self, buyer_id: str, seller_id: str, character_id: str, amount: float):
        async with await db.client.start_session() as session:
            async with session.start_transaction():
                await db.wallet_transactions.insert_one({
                    'user_id': buyer_id,
                    'type': 'purchase',
                    'amount': amount,
                    'character_id': character_id
                }, session=session)

                await db.characters.update_one(
                    {'_id': character_id, 'owner_id': seller_id},
                    {'$set': {'owner_id': buyer_id}},
                    session=session
                )

        return True


atomic_purchase_service = AtomicPurchaseService()
