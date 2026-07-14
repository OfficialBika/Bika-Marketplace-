from fastapi import APIRouter

router = APIRouter(prefix='/wallet', tags=['Wallet'])

@router.get('/balance/{user_id}')
async def balance(user_id: str):
    return {
        'user_id': user_id,
        'coin':'BKC',
        'balance':0
    }

@router.get('/history/{user_id}')
async def history(user_id: str):
    return {
        'user_id': user_id,
        'transactions':[]
    }
