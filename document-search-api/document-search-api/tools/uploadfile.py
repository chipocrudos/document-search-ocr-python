import io
from typing import Any
import uuid
from fastapi import Depends, Form, UploadFile
from config.bucket import s3_service, s3Config
from models.document import DocumentResponse


async def upload_file(
        file: UploadFile,
        indice: str = Form(...),
        tags: str = Form(...),
        bucket: Any = Depends(s3_service)
    ) -> DocumentResponse:
    unique_filename = f"{indice}/{uuid.uuid4().hex[:6]}_{file.filename}"

    contents = file.file.read()
    temp_file = io.BytesIO()
    temp_file.write(contents)
    temp_file.seek(0)
    bucket.upload_fileobj(temp_file, s3Config.BUCKET_NAME, unique_filename)
    temp_file.close()

    return DocumentResponse(
        indice=indice,
        tags=tags.split(",") if tags else None,
        path=unique_filename
    )
