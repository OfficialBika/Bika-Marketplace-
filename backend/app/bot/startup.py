"""Bot startup integration.

Import this from the existing Telegram bot startup after creating
bot application instance.
"""

from .register_web_command import register_web_command


def setup_bot_commands(application):
    register_web_command(application)
    return application
