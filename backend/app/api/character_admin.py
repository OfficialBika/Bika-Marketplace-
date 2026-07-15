from fastapi import APIRouter

router = APIRouter(prefix="/admin/characters", tags=["Admin Characters"])

@router.post("/")
async def create_character(data: dict):
    return {
        "success": True,
        "character": data
    }

@router.delete("/{character_id}")
async def delete_character(character_id: str):
    return {
        "success": True,
        "deleted": character_id
    }
