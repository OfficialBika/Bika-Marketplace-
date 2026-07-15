import logging
import os

from fastapi import APIRouter, Request
from telegram import Update

router = APIRouter()
logger = logging.getLogger(__name__)

WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")


@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    try:
        if WEBHOOK_SECRET:
            secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
            if secret != WEBHOOK_SECRET:
                logger.warning("Invalid Telegram webhook secret")
                return {"ok": False, "error": "invalid secret"}

        payload = await request.json()
        logger.info("Telegram update received: %s", payload.get("update_id"))

        application = getattr(request.app.state, "telegram_application", None)
        if application:
            update = Update.de_json(payload, application.bot)
            await application.process_update(update)

        return {"ok": True}

    except Exception as exc:
        logger.exception("Telegram webhook processing failed: %s", exc)
        return {"ok": False, "error": "processing_failed"}
