from fastapi import APIRouter

from app.security.telegram_auth import verify_telegram_data

router = APIRouter(prefix='/telegram', tags=['Telegram'])


@router.post('/auth')
async def telegram_auth(payload: dict):
    init_data = payload.get('init_data', '')
    bot_token = payload.get('bot_token', '')

    hash_value = verify_telegram_data(init_data, bot_token)

    return {
        'success': True,
        'telegram_hash': hash_value
    }
