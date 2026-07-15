from fastapi import APIRouter
import os

router = APIRouter(prefix="/config", tags=["Config"])

@router.get("/")
async def config():
    return {
        "rarity": os.getenv("SHOW_RARITY", "Supreme"),
        "marketplace": os.getenv("MARKETPLACE_ENABLED", "true")
    }
