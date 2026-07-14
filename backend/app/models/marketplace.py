from datetime import datetime


def listing_document(character_id, seller_id, price):
    return {
        "character_id": character_id,
        "seller_id": seller_id,
        "price": price,
        "coin": "BKC",
        "status": "active",
        "created_at": datetime.utcnow()
    }


def transaction_document(user_id, action, amount):
    return {
        "user_id": user_id,
        "action": action,
        "amount": amount,
        "coin": "BKC",
        "created_at": datetime.utcnow()
    }
