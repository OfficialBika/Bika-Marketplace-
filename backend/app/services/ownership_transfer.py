from datetime import datetime
from app.database.mongodb import db
from app.core.errors import TransactionError


async def transfer_character(character_id: str, old_owner: str, new_owner: str):
    if old_owner == new_owner:
        raise TransactionError('Invalid ownership transfer')

    result = await db.characters.update_one(
        {'_id': character_id, 'owner_id': old_owner},
        {'$set': {'owner_id': new_owner, 'updated_at': datetime.utcnow()}}
    )

    if result.modified_count == 0:
        raise TransactionError('Character ownership update failed')

    return {'status': 'completed', 'character_id': character_id}
