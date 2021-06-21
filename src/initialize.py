from typing import Dict, List, Tuple

from elasticsearch_dsl import Document, InnerDoc, Nested, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections


class Position(InnerDoc):
    start = Integer(required=True)
    end = Integer(required=True)


class SomeKey(InnerDoc):
    name = Text(required=True)
    positions = Nested(Position, multi=True)


class BasicInfo(Document):
    id = Keyword(required=True)
    text = Text(required=True)
    keys = Nested(SomeKey, multi=True)

    class Index:
        name = "basic-info-index"

    def __init__(
        self, id: int, text: str, keys: Dict[str, List[Tuple[int, int]]]
    ):
        _keys = []
        for name, val in keys.items():
            positions = [Position(start=x[0], end=x[1]) for x in val]
            _keys.append(SomeKey(name=name, positions=positions))

        super().__init__(id=id, text=text, keys=_keys)

    def save(self, **kwargs):
        return super().save(**kwargs)


if __name__ == "__main__":
    connections.create_connection(hosts=["localhost:9200"])

    BasicInfo.init()

    article = BasicInfo(
        id=0, 
        text="aaa bbb aaa", 
        keys={"aaa": [(0, 2), (8, 10)], "bbb": [(4, 6)]}
    )
    article.save()

    article = BasicInfo(
        id=1, 
        text="aaa aaa", 
        keys={"aaa": [(0, 2), (4, 6)]}
    )
    article.save()

    article = BasicInfo(
        id=2, 
        text="bbb", 
        keys={"bbb": [(0, 2)]}
    )
    article.save()
