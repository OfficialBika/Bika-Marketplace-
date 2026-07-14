from fastapi import APIRouter
from app.services.order_service import create_order

router = APIRouter(prefix='/orders', tags=['Orders'])

@router.post('/')
async def create(user_id: str, character_id: str, amount: float):
    return await create_order(user_id, character_id, amount)
