from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/stats")
async def stats():
    return {
        "users": 0,
        "characters": 0,
        "trades": 0
    }

@router.get("/health")
async def health():
    return {"status":"admin_api_ok"}
