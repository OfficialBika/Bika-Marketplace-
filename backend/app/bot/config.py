import os


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
WEB_APP_URL = os.getenv("WEB_APP_URL", "")
BOT_MODE = os.getenv("BOT_MODE", "polling")


def bot_configured():
    return bool(TELEGRAM_BOT_TOKEN and WEB_APP_URL)
