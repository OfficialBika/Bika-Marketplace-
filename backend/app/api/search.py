from fastapi import APIRouter

router = APIRouter(prefix='/search', tags=['Search'])

@router.get('/')
async def search(q: str = '', rarity: str = ''):
    return {
        'query': q,
        'rarity': rarity,
        'items': []
    }
