from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.purchase_service import create_purchase

router = APIRouter(
    prefix="/purchase",
    tags=["Purchase"]
)


class PurchaseRequest(BaseModel):
    user_id: str
    character_id: str
    amount: float


@router.post("/")
async def purchase_character(data: PurchaseRequest):
    try:
        result = await create_purchase(
            user_id=data.user_id,
            character_id=data.character_id,
            amount=data.amount
        )

        return {
            "success": True,
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
