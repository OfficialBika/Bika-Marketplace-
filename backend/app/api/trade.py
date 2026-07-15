from fastapi import APIRouter

router = APIRouter(prefix="/trade", tags=["Trade"])

@router.get("/")
async def trades():
    return {"trades":[]}
