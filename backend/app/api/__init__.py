from .auth import router as auth_router
from .characters import router as characters_router
from .wallet import router as wallet_router
from .trade import router as trade_router

__all__ = [
    'auth_router',
    'characters_router',
    'wallet_router',
    'trade_router'
]
