"""
Telegram /web command handler.

Wire this handler into the existing Telegram bot startup to enable
sending a Mini App open button.
"""

import os

WEB_APP_URL = os.getenv("WEB_APP_URL", "https://YOUR_FRONTEND.onrender.com")


def build_web_button():
    return {
        "text": "Open Bika Marketplace",
        "web_app": {
            "url": WEB_APP_URL
        }
    }


async def web_command(update, context):
    keyboard = [[build_web_button()]]
    await update.message.reply_text(
        "Open Bika Marketplace Mini App:",
        reply_markup={"inline_keyboard": keyboard}
    )
