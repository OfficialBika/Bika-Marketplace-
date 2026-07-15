import logging
import os

from fastapi import APIRouter, Request
from telegram import Update

router = APIRouter()
logger = logging.getLogger(__name__)

WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")

# Lightweight in-memory protection for duplicate Telegram deliveries.
processed_updates = set()
MAX_CACHE_SIZE = 1000


@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    try:
        if WEBHOOK_SECRET:
            secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
            if secret != WEBHOOK_SECRET:
                logger.warning("Invalid Telegram webhook secret")
                return {"ok": False, "error": "invalid secret"}

        payload = await request.json()
        update_id = payload.get("update_id")
        logger.info("Telegram update received: %s", update_id)

        if update_id in processed_updates:
            return {"ok": True, "duplicate": True}

        if update_id is not None:
            processed_updates.add(update_id)
            if len(processed_updates) > MAX_CACHE_SIZE:
                processed_updates.clear()

        application = getattr(request.app.state, "telegram_application", None)
        if application:
            update = Update.de_json(payload, application.bot)
            await application.process_update(update)

        return {"ok": True}

    except Exception as exc:
        logger.exception("Telegram webhook processing failed: %s", exc)
        return {"ok": False, "error": "processing_failed"}
