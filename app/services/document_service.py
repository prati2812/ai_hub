from fastapi import UploadFile
import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


async def upload(file: UploadFile):

    contents = await file.read()

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
       f.write(contents)


    return {
        "filename" : file.filename,
        "content_type": file.content_type,
        "size": len(contents),
        "path": file_path
    }

    
