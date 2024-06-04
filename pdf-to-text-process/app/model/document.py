from dataclasses import dataclass
from typing import List, Protocol


class ProtoDocument(Protocol):
    index : str
    tags : List[str]
    path: str
    page: int
    content : str
    
    @classmethod
    def create_document(
            cls, index: str, tags: List[str], path: str, page: int, content: str
        ) -> 'ProtoDocument':
        ...


@dataclass
class Document:
    index : str
    tags : List[str]
    path: str
    page: int
    content : str

    @classmethod
    def create_document(
        cls, index: str, tags: List[str], path: str, page: int, content: str
    ) -> 'Document':
        return cls(index, tags, path, page, content)
