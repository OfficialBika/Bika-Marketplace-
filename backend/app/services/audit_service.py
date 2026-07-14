from datetime import datetime
from app.database.mongodb import db

async def create_audit_log(action: str, user_id: str, detail: dict):
    return await db.audit_logs.insert_one({
        'action': action,
        'user_id': user_id,
        'detail': detail,
        'created_at': datetime.utcnow()
    })
