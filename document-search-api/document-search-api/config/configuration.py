import base64
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):

    KEY: str
    CORS_DOMAINS: list[str]

    class Config:
        env_prefix = ""
        case_sensitive = True


class S3Config(BaseSettings):

    ENDPOINT_URL: str
    SERVICE_NAME: str = "s3"
    ACCESS_KEY: str
    SECRET_KEY: str
    BUCKET_NAME: str
    PUBLIC_EXP_TIME: int

    class Config:
        env_prefix = ""
        case_sensitive = True


class RabbitConfig(BaseSettings):

    RABBITMQ_HOST: str
    RABBITMQ_QUEUE: str
  
    class Config:
        env_prefix = ""
        case_sensitive = True


class ZincConfig(BaseSettings):

    ZINC_HOST: str
    ZINC_USERNAME: str
    ZINC_PASSWORD: str

    def __post_init__(self):
        if not self.ZINC_HOST or not self.ZINC_USERNAME or not self.ZINC_PASSWORD:
            raise ValueError("Zinc credentials not set")

    @property
    def ZINC_CRED(self) -> str:
        return base64.b64encode(
                    bytes(self.ZINC_USERNAME + ":" + self.ZINC_PASSWORD, "utf-8")
                ).decode("utf-8")


    def get_all_index_api(self) -> str:
        return f"{self.ZINC_HOST}/api/index_name?name="

    def get_index_search_api(self, index: str) -> str:
        return f"{self.ZINC_HOST}/api/{index}/_search"

    def get_es_index_search_api(self, index: str) -> str:
        return f"{self.ZINC_HOST}/es/{index}/_search"


appConfig = AppConfig() # type: ignore
s3Config = S3Config()   # type: ignore
rabbitmqConfig = RabbitConfig() # type: ignore
zincConfig = ZincConfig() # type: ignore
