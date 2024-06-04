from dataclasses import dataclass
from typing import Any, List
from config.configuration import ZincConfig
from model.document import ProtoDocument



@dataclass
class ZincSearch:

    config: ZincConfig
    client: Any

    def __post_init__(self):
        self.HEADERS = {
            "Content-type": "application/json",
            "Authorization": f"Basic {self.config.ZINC_CRED}"
        }

    def create_document(self, document: ProtoDocument) :
        r = self.client.post(
            self.config.create_index_api(document.index),
            headers=self.HEADERS,
            json=document.__dict__
        )
        return r.json()


    def create_bulk_documents(self, index: str, documents: List[ProtoDocument]):
        r = self.client.post(
            self.config.create_bulk_api(),
            headers=self.HEADERS,
            json={
                "index": index,
                "records": [doc.__dict__ for doc in documents]
            }
        )

        return r.json()
