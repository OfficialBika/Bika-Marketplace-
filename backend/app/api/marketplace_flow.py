from fastapi import APIRouter

router = APIRouter(prefix="/marketplace-flow", tags=["Marketplace Flow"])

@router.get("/status")
async def status():
    return {"ready": True}
