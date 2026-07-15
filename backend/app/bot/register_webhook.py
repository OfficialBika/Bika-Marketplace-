import os

import httpx


async def register_telegram_webhook():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    webhook_url = os.getenv("RENDER_API_URL") + "/telegram/webhook"
    secret = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")

    if not token or not webhook_url:
        return {"ok": False, "error": "missing configuration"}

    url = f"https://api.telegram.org/bot{token}/setWebhook"
    payload = {
        "url": webhook_url,
    }

    if secret:
        payload["secret_token"] = secret

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()
