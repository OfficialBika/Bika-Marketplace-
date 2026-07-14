import hmac
import hashlib


def verify_telegram_data(data: str, bot_token: str):
    secret = hashlib.sha256(bot_token.encode()).digest()
    check = hmac.new(secret, data.encode(), hashlib.sha256).hexdigest()
    return check
