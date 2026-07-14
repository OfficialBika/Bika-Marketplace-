async def create_indexes(db):
    await db.marketplace_listings.create_index('character_id')
    await db.marketplace_listings.create_index('status')
    await db.marketplace_orders.create_index('user_id')
    await db.auctions.create_index('character_id')
    await db.bids.create_index('auction_id')
    await db.wallet_transactions.create_index('user_id')
    await db.audit_logs.create_index('user_id')
