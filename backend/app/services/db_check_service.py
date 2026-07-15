from app.database.mongodb import db

async def check_database():
    try:
        await db.command("ping")
        return {"database": "connected"}
    except Exception as e:
        return {"database": "error", "message": str(e)}
