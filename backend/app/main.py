from fastapi import FastAPI

app = FastAPI(title='Bika Marketplace API')


@app.get('/health')
async def health():
    return {
        'status': 'ok',
        'service': 'bika-marketplace'
    }


@app.get('/')
async def root():
    return {'name': 'Bika Marketplace', 'coin': 'BKC', 'status': 'running'}
