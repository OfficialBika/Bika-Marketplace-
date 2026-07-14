from fastapi import APIRouter
from app.services.character_service import get_character, get_user_characters

router = APIRouter(prefix='/characters', tags=['Characters'])

@router.get('/{character_id}')
async def detail(character_id: str):
    return await get_character(character_id)

@router.get('/user/{user_id}')
async def inventory(user_id: str):
    return await get_user_characters(user_id)
