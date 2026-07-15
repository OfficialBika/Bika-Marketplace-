from fastapi import APIRouter
from app.services.auction_service import create_bid

router = APIRouter(prefix="/auction", tags=["Auction"])

@router.post("/bid")
async def bid(data:dict):
    return await create_bid(
        str(data.get("user_id")),
        str(data.get("auction_id")),
        float(data.get("amount",0))
    )
