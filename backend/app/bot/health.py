from fastapi import APIRouter

router = APIRouter()


@router.get("/telegram/status")
async def telegram_status():
    return {
        "service": "telegram-webhook",
        "status": "ready"
    }
