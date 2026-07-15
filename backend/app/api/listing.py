from fastapi import APIRouter

router = APIRouter(prefix="/listing", tags=["Listing"])

@router.get("/")
async def listings():
    return {
        "success": True,
        "items": []
    }

@router.post("/")
async def create_listing(data: dict):
    return {
        "success": True,
        "listing": data
    }
