from dataclasses import dataclass
import os
import base64


def get_env_integer(name: str, default: int) -> int:
    return int(os.getenv(name, default))


@dataclass(frozen=True)
class Appconfig:
    ASYNCRONOUS_SEMAPHORE : int = get_env_integer("ASYNCRONOUS_SEMAPHORE", 3)


@dataclass (frozen=True)
class S3Config:

    ENDPOINT_URL: str | None = os.getenv("ENDPOINT_URL")
    ACCESS_KEY: str | None = os.getenv("ACCESS_KEY")
    SECRET_KEY: str | None = os.getenv("SECRET_KEY")
    BUCKET_NAME: str | None = os.getenv("BUCKET_NAME")
    SERVICE_NAME: str | None = os.getenv("SERVICE_NAME", "s3")


@dataclass(frozen=True)
class RabbitConfig:

    RABBITMQ_HOST: str | None = os.getenv("RABBITMQ_HOST")
    RABBITMQ_QUEUE: str | None = os.getenv("RABBITMQ_QUEUE")
    RABBITMQ_PREFETCH_COUNT: int = get_env_integer("RABBITMQ_PREFETCH_COUNT", 1)


@dataclass
class ZincConfig:

    ZINC_HOST: str | None = os.getenv("ZINC_HOST")
    ZINC_USERNAME: str | None = os.getenv("ZINC_USERNAME")
    ZINC_PASSWORD: str | None = os.getenv("ZINC_PASSWORD")
    __creds: str = ""

    def __post_init__(self):
        if not self.ZINC_HOST or not self.ZINC_USERNAME or not self.ZINC_PASSWORD:
            raise ValueError("Zinc credentials not set")
        self.__creds = base64.b64encode(
                    bytes(self.ZINC_USERNAME + ":" + self.ZINC_PASSWORD, "utf-8")
                ).decode("utf-8")

    @property
    def ZINC_CRED(self) -> str:
        return self.__creds

    def create_index_api(self, index: str) -> str:
        return f"{self.ZINC_HOST}/api/{index}/document"

    def create_bulk_api(self) -> str:
        return f"{self.ZINC_HOST}/api/_bulkv2"


appConfig = Appconfig()
s3Config = S3Config()
rabbitmqConfig = RabbitConfig()
zincConfig = ZincConfig()