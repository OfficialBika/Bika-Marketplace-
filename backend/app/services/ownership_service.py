from app.core.errors import TransactionError
from app.database.mongodb import db

async def transfer_ownership(character_id: str, from_user: str, to_user: str):
    if from_user == to_user:
        raise TransactionError('Cannot transfer to same owner')

    await db.characters.update_one(
        {"_id": character_id, "owner_id": from_user},
        {"$set": {"owner_id": to_user}}
    )

    return {
        'character_id': character_id,
        'from': from_user,
        'to': to_user,
        'status': 'completed'
    }
