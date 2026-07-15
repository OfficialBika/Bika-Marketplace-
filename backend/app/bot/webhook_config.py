import os


TELEGRAM_API_URL = "https://api.telegram.org"
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
RENDER_API_URL = os.getenv("RENDER_API_URL", "")
WEBHOOK_PATH = "/telegram/webhook"


def get_webhook_url():
    return f"{RENDER_API_URL}{WEBHOOK_PATH}"
