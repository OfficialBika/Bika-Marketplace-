from app.core.errors import TransactionError

async def transfer_ownership(character_id: str, from_user: str, to_user: str):
    if from_user == to_user:
        raise TransactionError('Cannot transfer to same owner')

    return {
        'character_id': character_id,
        'from': from_user,
        'to': to_user,
        'status': 'pending'
    }
