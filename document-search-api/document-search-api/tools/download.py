from typing import Any
from fastapi import Depends, UploadFile
from config.bucket import s3_service, s3Config
from models.document import DocumentResponse, DocumentURl
import io
import uuid
import httpx


async def download_file(document: DocumentURl) -> UploadFile:
    async with httpx.AsyncClient() as client:
        r = await client.get(document.url)
        fn = document.url.split('/')[-1]

        return UploadFile(filename=fn, file=io.BytesIO(r.content), headers=r.headers)


async def upload_from_url(
        document: DocumentURl,
        file: UploadFile = Depends(download_file),
        bucket: Any = Depends(s3_service)
    ) -> DocumentResponse:
    name = file.filename
    if file.content_type is None:
        name = ""

    unique_filename = f"{document.index}/{uuid.uuid4().hex[:6]}_{name}"


    contents = file.file.read()
    temp_file = io.BytesIO()
    temp_file.write(contents)
    temp_file.seek(0)
    bucket.upload_fileobj(temp_file, s3Config.BUCKET_NAME, unique_filename)
    temp_file.close()

    return DocumentResponse(
        index=document.index,
        tags=document.tags,
        path=unique_filename
    )
