from pydantic import BaseModel


class Document(BaseModel):
    index : str
    tags: list[str] | None


class DocumentURl(Document):
    url : str


class DocumentResponse(Document):
    path : str