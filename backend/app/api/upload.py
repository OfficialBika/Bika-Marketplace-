from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    return {
        "success": True,
        "filename": file.filename,
        "url": f"/uploads/{file.filename}"
    }
