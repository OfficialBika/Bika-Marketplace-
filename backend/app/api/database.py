from fastapi import APIRouter
from app.services.db_check_service import check_database

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/database")
async def database():
    return await check_database()
