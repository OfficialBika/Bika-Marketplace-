def validate_purchase(data: dict):
    required = ["user_id", "character_id", "amount"]
    return all(k in data for k in required)

def validate_listing(data: dict):
    required = ["character_id", "price"]
    return all(k in data for k in required)
