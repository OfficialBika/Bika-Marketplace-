"""
Telegram /web command handler.

Sends a Telegram Mini App launch button using python-telegram-bot v21 API.
"""

import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

WEB_APP_URL = os.getenv("WEB_APP_URL", "https://YOUR_FRONTEND.onrender.com")


def build_web_button():
    return InlineKeyboardButton(
        text="Open Bika Marketplace",
        web_app=WebAppInfo(url=WEB_APP_URL),
    )


async def web_command(update, context):
    keyboard = [[build_web_button()]]

    await update.message.reply_text(
        "Open Bika Marketplace Mini App:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )
