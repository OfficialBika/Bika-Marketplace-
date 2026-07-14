from fastapi import APIRouter

from app.api import marketplace, wallet, orders, search, health, characters, purchase

api_router = APIRouter()

api_router.include_router(marketplace.router)
api_router.include_router(wallet.router)
api_router.include_router(orders.router)
api_router.include_router(search.router)
api_router.include_router(health.router)
api_router.include_router(characters.router)
api_router.include_router(purchase.router)
