"""Register /web command on Telegram bot.

Uses python-telegram-bot v21 CommandHandler API.
"""

from telegram.ext import CommandHandler

from .web_command import web_command


def register_web_command(application):
    application.add_handler(
        CommandHandler("web", web_command)
    )
