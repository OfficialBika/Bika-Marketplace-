import logging
import os

from fastapi import APIRouter, Request

router = APIRouter()
logger = logging.getLogger(__name__)

WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")


@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    if WEBHOOK_SECRET:
        secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
        if secret != WEBHOOK_SECRET:
            logger.warning("Invalid Telegram webhook secret")
            return {"ok": False, "error": "invalid secret"}

    update = await request.json()

    logger.info("Telegram update received: %s", update.get("update_id"))

    # Telegram Application processing hook.
    # Connect application.process_update(update) here when the bot instance
    # is attached to FastAPI state.
    application = getattr(request.app.state, "telegram_application", None)
    if application:
        await application.process_update(update)

    return {"ok": True}
