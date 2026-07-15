import os


def telegram_config_status():
    required = {
        "TELEGRAM_BOT_TOKEN": os.getenv("TELEGRAM_BOT_TOKEN"),
        "WEB_APP_URL": os.getenv("WEB_APP_URL"),
        "RENDER_API_URL": os.getenv("RENDER_API_URL"),
    }

    return {
        "ready": all(required.values()),
        "configured": {
            key: bool(value)
            for key, value in required.items()
        },
    }
