from fastapi import APIRouter, Query

from app.services.marketplace_service import marketplace_service

router = APIRouter(prefix='/marketplace', tags=['Marketplace'])


@router.get('/status')
async def status():
    return {
        'service': 'Bika Marketplace',
        'coin': 'BKC',
        'status': 'ready'
    }


@router.get('/features')
async def features():
    return {
        'features': [
            'Bika Characters',
            'Marketplace',
            'Auction',
            'Trade',
            'Spin Wheel',
            'Wallet History'
        ]
    }


@router.get('/')
async def list_marketplace(
    limit: int = Query(default=20, le=100),
    rarity: str | None = None
):
    items = await marketplace_service.get_items(limit, rarity)

    return {
        'success': True,
        'data': items
    }
