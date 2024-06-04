from dataclasses import dataclass
from typing import Any, List, Set
from config.configuration import ZincConfig
from models.search import Document, Indexes, Tags


@dataclass
class ZincSearch:

    config: ZincConfig
    client: Any

    def __post_init__(self):
        self.HEADERS = {
            "Content-type": "application/json",
            "Authorization": f"Basic {self.config.ZINC_CRED}"
        }

    def get_all_index(self) -> Indexes:
        r = self.client.get(
            self.config.get_all_index_api(),
            headers=self.HEADERS
        )

        indexes = Indexes(indexes=r.json())
        return indexes

    def get_index_tags(self, index: str) -> Tags:
        r = self.client.get(
            self.config.get_index_search_api(index),
            headers=self.HEADERS
        )
        params = { # type: ignore
            "_source": [ "tags" ],
            "query": {
                "match_all": {},
            }
        }

        r = self.client.post(
        self.config.get_index_search_api(index),
        headers=self.HEADERS,
        json=params
    )
        tags: Set[str] = set()
        for hit in r.json()["hits"]["hits"]:
            tags.update(hit["_source"]["tags"])

        return Tags(tags=list(tags))

    def get_search(self, index: str, tags: str, content: str) -> List[Document]:
        
        r = self.client.get(
                self.config.get_index_search_api(index),
                headers=self.HEADERS
            )
        params = { # type: ignore
             "query": {
                 "bool":{ 
                    "should": {
                        "match_phrase": { "content": content,},
                        "match_phrase": { "tags": tags },
                    },
                }
            },
            "track_total_hits": True,

        }

        r = self.client.post(
            self.config.get_index_search_api(index),
            headers=self.HEADERS,
            json=params
        )

        documents: List[Document] = []
        for hit in r.json()["hits"]["hits"]:
            documents.append(
                Document(
                    _id=hit["_id"],
                    index=hit["_source"]["index"],
                    tags=hit["_source"]["tags"],
                    content=hit["_source"]["content"],
                    page=hit["_source"]["page"],
                    path=hit["_source"]["path"],
                    _score=hit["_score"]
                )
            )
    
        return documents

