from fastapi import APIRouter
from app.services.health_service import service_status

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/status")
async def status():
    return await service_status()
