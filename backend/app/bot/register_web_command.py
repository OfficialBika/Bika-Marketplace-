"""Register /web command on Telegram bot.

Call register_web_command(application) from the bot startup after
creating the Telegram application instance.
"""

from .web_command import web_command


def register_web_command(application):
    application.add_handler(
        application.command_handler("web", web_command)
    )
