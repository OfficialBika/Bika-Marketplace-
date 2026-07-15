from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/stats")
async def stats():
    return {
        "users": 0,
        "characters": 0,
        "orders": 0,
        "auctions": 0
    }
