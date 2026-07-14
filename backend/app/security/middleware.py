from fastapi import Header, HTTPException

from app.security.jwt import verify_token


async def auth_user(authorization: str | None = Header(default=None)):
    if not authorization:
        raise HTTPException(status_code=401, detail='Missing token')

    token = authorization.replace('Bearer ', '')

    try:
        return verify_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail='Invalid token')
