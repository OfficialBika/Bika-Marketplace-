from fastapi import APIRouter

from app.services.purchase_service import purchase_service

router = APIRouter(prefix='/marketplace', tags=['Purchase'])


@router.post('/buy')
async def buy_character(payload: dict):
    result = await purchase_service.buy_character(
        payload.get('buyer_id'),
        payload.get('seller_id'),
        payload.get('character_id'),
        payload.get('amount', 0)
    )

    return {
        'success': True,
        'data': result
    }
