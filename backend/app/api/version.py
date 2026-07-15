from fastapi import APIRouter

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/version")
async def version():
    return {
        "name": "Bika Marketplace",
        "version": "v22",
        "status": "running"
    }
