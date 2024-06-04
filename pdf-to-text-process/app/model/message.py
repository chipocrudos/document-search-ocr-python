

from dataclasses import dataclass
import json


@dataclass()
class Message:
    index : str
    tags: list[str]
    path : str

    @classmethod
    def create_message(cls, notifiacation: str) -> 'Message':
        try:

            js = json.loads(notifiacation)
            index = js["index"]
            tags = js["tags"]
            path = js["path"]

        except json.JSONDecodeError:
            raise ValueError("Invalid Message Format")

        return cls(index, tags, path)
