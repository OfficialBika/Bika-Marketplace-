import os

from fastapi import APIRouter, Request

router = APIRouter()

WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")


@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    if WEBHOOK_SECRET:
        secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret != WEBHOOK_SECRET:
            return {"ok": False, "error": "invalid secret"}

    update = await request.json()

    # Pass update to Telegram application handler here.
    # The /web Mini App command is registered through setup_bot_commands.
    return {"ok": True}
