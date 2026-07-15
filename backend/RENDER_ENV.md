# Render Environment Setup

Backend Web Service variables:

```env
PORT=8000
BOT_MODE=webhook
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_WEBHOOK_SECRET=your_secret
TELEGRAM_WEBHOOK_PATH=/telegram/webhook
RENDER_API_URL=https://your-api.onrender.com
WEB_APP_URL=https://your-frontend.onrender.com
```

After deployment:

1. Check `/health`
2. Check `/telegram/status`
3. Confirm Telegram webhook points to:

```
https://your-api.onrender.com/telegram/webhook
```
