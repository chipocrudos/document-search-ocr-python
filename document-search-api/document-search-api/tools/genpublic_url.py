from config.bucket import s3, s3Config


def genpublic_url(key: str) -> str:
    return s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": s3Config.BUCKET_NAME,
            "Key": key,
        },
        ExpiresIn=s3Config.PUBLIC_EXP_TIME,
    )
    