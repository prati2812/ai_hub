from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_service import upload

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )
    
    result = await upload(file)


    return result