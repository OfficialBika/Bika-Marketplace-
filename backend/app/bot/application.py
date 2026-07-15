import os

from telegram.ext import Application

from .config import TELEGRAM_BOT_TOKEN
from .startup import setup_bot_commands


async def create_telegram_application():
    if not TELEGRAM_BOT_TOKEN:
        return None

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    setup_bot_commands(application)
    await application.initialize()
    return application
