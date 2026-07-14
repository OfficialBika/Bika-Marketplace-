from datetime import datetime

# MongoDB document examples

NFT_COLLECTION = 'bika_characters'
AUCTION_COLLECTION = 'auctions'
TRANSACTION_COLLECTION = 'wallet_transactions'
SPIN_HISTORY_COLLECTION = 'spin_history'


def transaction_document(user_id, title, amount, tx_type):
    return {
        'user_id': user_id,
        'title': title,
        'amount': amount,
        'type': tx_type,
        'created_at': datetime.utcnow()
    }
