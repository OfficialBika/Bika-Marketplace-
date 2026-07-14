from datetime import datetime
from app.database.mongodb import db


class AuditRepository:
    async def log(self, action: str, data: dict):
        await db.audit_logs.insert_one({
            'action': action,
            'data': data,
            'created_at': datetime.utcnow()
        })


audit_repository = AuditRepository()
