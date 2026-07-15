from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/readiness")
async def readiness():
    return {
        "api": True,
        "marketplace": True,
        "ready": True
    }
