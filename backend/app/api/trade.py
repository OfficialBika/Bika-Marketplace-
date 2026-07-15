from fastapi import APIRouter

router = APIRouter(prefix='/trade', tags=['Trade'])


@router.get('/history/{user_id}')
async def history(user_id: str):
    return {
        'user_id': user_id,
        'trades': []
    }


@router.post('/')
async def create_trade(payload: dict):
    return {
        'success': True,
        'trade': payload
    }
