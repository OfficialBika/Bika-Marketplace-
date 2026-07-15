from fastapi import APIRouter

router = APIRouter(prefix="/marketplace", tags=["Marketplace"])

@router.post("/listing")
async def create_listing(data: dict):
    return {"success": True, "listing": data}

@router.get("/listings")
async def get_listings():
    return {"success": True, "listings": []}
