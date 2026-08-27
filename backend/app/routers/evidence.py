from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
from app.models.schemas import UploadResponse
from app.services.parser import ForensicParser

router = APIRouter(prefix="/api/v1/evidence", tags=["evidence"])

UPLOAD_DIR = "data/uploads"

@router.post("/upload", response_model=UploadResponse)
async def upload_evidence(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    file_id = str(uuid.uuid4())
    ext = os.path.splitext(file.filename)[1]
    saved_filename = f"{file_id}{ext}"
    file_path = os.path.join(UPLOAD_DIR, saved_filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return UploadResponse(
        filename=file.filename,
        message="File uploaded successfully",
        file_id=file_id
    )
