from fastapi import APIRouter

router = APIRouter(prefix="/wallet", tags=["Wallet"])

@router.get("/{user_id}")
async def get_wallet(user_id:str):
    return {
        "user_id": user_id,
        "balance": 0,
        "currency": "BKC",
        "transactions": []
    }
