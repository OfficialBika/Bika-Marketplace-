from fastapi import APIRouter

from app.services.character_service import character_service

router = APIRouter(prefix='/characters', tags=['Characters'])


@router.get('/{character_id}')
async def detail(character_id: str):
    character = await character_service.get_character(character_id)

    if not character:
        return {
            'success': False,
            'message': 'Character not found'
        }

    return {
        'success': True,
        'data': character
    }


@router.get('/inventory/{user_id}')
async def inventory(user_id: str):
    items = await character_service.get_user_characters(user_id)

    return {
        'success': True,
        'characters': items
    }


@router.get('/featured')
async def featured():
    import os
    rarity = os.getenv('SHOW_RARITY', 'Supreme')
    limit = int(os.getenv('FEATURED_LIMIT', '8'))

    items = await character_service.get_featured_characters(
        rarity=rarity,
        limit=limit
    )

    return {
        'success': True,
        'rarity': rarity,
        'characters': items
    }
