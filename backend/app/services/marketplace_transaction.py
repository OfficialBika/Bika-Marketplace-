from app.core.errors import TransactionError

async def execute_transaction(action):
    try:
        result = await action()
        return result
    except Exception as exc:
        raise TransactionError(str(exc), 'TRANSACTION_FAILED')
