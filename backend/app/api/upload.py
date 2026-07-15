from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload(file: UploadFile = File(...)):
    return {
        "success": True,
        "filename": file.filename
    }
