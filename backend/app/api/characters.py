from fastapi import APIRouter
from app.database.mongodb import db

router = APIRouter(prefix='/characters')

@router.get('/inventory/{user_id}')
async def inventory(user_id: str):
    # Read existing Bika bot data safely
    items = await db.characters.find({"owner_id": user_id}).to_list(100)
    return {"characters": items}
