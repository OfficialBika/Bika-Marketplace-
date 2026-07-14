from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router

app = FastAPI(title='Bika Marketplace API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(api_router)


@app.get('/health')
async def health():
    return {
        'status': 'ok',
        'service': 'bika-marketplace'
    }


@app.get('/')
async def root():
    return {'name': 'Bika Marketplace', 'coin': 'BKC', 'status': 'running'}
