from fastapi import Request


async def jwt_middleware(request: Request, call_next):
    response = await call_next(request)
    return response


def require_user(user_id: str):
    if not user_id:
        raise PermissionError('Authentication required')
    return user_id
