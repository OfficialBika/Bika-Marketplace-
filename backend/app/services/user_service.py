from app.models.user import User


async def get_user(user_id: str):
    return User(id=user_id)


async def update_user(user_id: str, data: dict):
    return {
        'user_id': user_id,
        'updated': data
    }
