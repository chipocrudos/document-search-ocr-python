
from typing import Protocol
from typing import List
from model.document import ProtoDocument


class ProtoRepository(Protocol):
    def create_document(self, document: ProtoDocument) :
        pass

    def create_bulk_documents(self, index:str, documents: List[ProtoDocument]):
        pass
