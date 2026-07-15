from fastapi import APIRouter

router = APIRouter(prefix="/marketplace", tags=["Marketplace Flow"])

@router.get("/status")
async def status():
    return {
        "enabled": True,
        "marketplace": "Bika Marketplace"
    }

@router.post("/exchange")
async def exchange(data: dict):
    return {
        "success": True,
        "exchange": data
    }
