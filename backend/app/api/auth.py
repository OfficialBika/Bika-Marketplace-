from fastapi import APIRouter
from app.services.auth_service import create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/telegram")
async def telegram_login(data: dict):
    user_id = str(data.get("id"))
    return {
        "success": True,
        "token": create_token(user_id),
        "user_id": user_id
    }
