from typing import Any

from .configuration import s3Config
import boto3

s3 = boto3.client( # type: ignore
        s3Config.SERVICE_NAME, # type: ignore
        endpoint_url=s3Config.ENDPOINT_URL,
        aws_access_key_id=s3Config.ACCESS_KEY,
        aws_secret_access_key=s3Config.SECRET_KEY
    ) # type: ignore

async def s3_service() -> Any:
    yield s3
