from datetime import datetime

async def settle_auction(auction_id: str, winner_id: str):
    return {
        'auction_id': auction_id,
        'winner_id': winner_id,
        'status': 'settled',
        'settled_at': datetime.utcnow()
    }
