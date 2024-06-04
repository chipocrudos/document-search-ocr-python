import string
from typing import Any
from .configuration import s3Config
import boto3
from botocore.config import Config

def s3_service() -> Any:
    session = boto3.session.Session()

    return session.client( # type: ignore
        s3Config.SERVICE_NAME, # type: ignore
        endpoint_url=s3Config.ENDPOINT_URL,
        aws_access_key_id=s3Config.ACCESS_KEY,
        aws_secret_access_key=s3Config.SECRET_KEY,
        config=Config(signature_version='s3v4')
    ) # type: ignore


def s3_bucket() -> Any:

    s3_client = s3_service()

    def client(file: string, folder: str) -> str:
        filename: str = file.split('/')[-1]
        
        with open(f'{folder}/{filename}', 'wb') as f:
            s3_client.download_fileobj(s3Config.BUCKET_NAME, file, f)    

        return filename
    
    return client