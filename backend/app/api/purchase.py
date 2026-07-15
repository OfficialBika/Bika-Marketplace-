from fastapi import APIRouter
from app.services.purchase_service import create_order

router = APIRouter(prefix="/purchase", tags=["Purchase"])

@router.post("/")
async def purchase(data: dict):
    return await create_order(
        str(data.get("user_id")),
        str(data.get("character_id")),
        float(data.get("amount", 0))
    )
