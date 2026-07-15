# Telegram Mini App Bot Integration

## Enable /web command

After creating the Telegram bot application, connect the command setup:

```python
from app.bot.startup import setup_bot_commands

setup_bot_commands(application)
```

Required environment variable:

```env
WEB_APP_URL=https://YOUR_FRONTEND.onrender.com
```

The `/web` command sends an inline Mini App button that opens the marketplace web app.
