from fastapi import Request
from fastapi.responses import JSONResponse


class MarketplaceException(Exception):
    def __init__(self, message: str, code: str = 'MARKETPLACE_ERROR'):
        self.message = message
        self.code = code


async def marketplace_exception_handler(request: Request, exc: MarketplaceException):
    return JSONResponse(
        status_code=400,
        content={
            'success': False,
            'error': exc.code,
            'message': exc.message
        }
    )
