from pydantic import BaseModel, computed_field
from tools.genpublic_url import genpublic_url


class Tags (BaseModel):
    tags: list[str]


class Index (BaseModel):
    index: str


class Indexes (BaseModel):
    indexes: list[str]


class Document (BaseModel):
    _id: str
    index: str
    tags: list[str]
    content: str
    page: int
    path: str
    _score: float

    @computed_field
    def url(self) -> str:
        return genpublic_url(self.path)


class DocumentSearch (BaseModel):
    tags: str
    content: str


