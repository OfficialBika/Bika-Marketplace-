from fastapi import APIRouter

from app.services.wallet_service import wallet_service

router = APIRouter(prefix='/wallet', tags=['Wallet'])


@router.get('/balance/{user_id}')
async def balance(user_id: str):
    wallet = await wallet_service.get_wallet(user_id)

    return wallet


@router.get('/history/{user_id}')
async def history(user_id: str):
    wallet = await wallet_service.get_wallet(user_id)

    return {
        'user_id': user_id,
        'coin': wallet['coin'],
        'transactions': wallet['transactions']
    }
