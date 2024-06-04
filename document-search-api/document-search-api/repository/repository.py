
from typing import List, Protocol
from models.search import Document, Indexes, Tags


class ProtoRepository(Protocol):
    def get_all_index(self) -> Indexes:
        ...

    def get_index_tags(self, index: str) -> Tags:
        ...

    def get_search(self, index: str, tags: str, content: str) -> List[Document]:
        ...
