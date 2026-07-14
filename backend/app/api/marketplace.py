from fastapi import APIRouter

router = APIRouter(prefix='/marketplace', tags=['Marketplace'])

@router.get('/status')
async def status():
    return {
        'service':'Bika Marketplace',
        'coin':'BKC',
        'status':'ready'
    }

@router.get('/features')
async def features():
    return {
        'features':[
            'Bika Characters',
            'NFT Marketplace',
            'Auction',
            'Trade',
            'Spin Wheel',
            'Wallet History'
        ]
    }
