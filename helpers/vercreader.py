# -*- coding: utf-8 -*-

import collections
import json
import uuid
from functools import reduce


def read_verc(verc_json):
    # забираем из списка абзацы и чанки
    indents = [
        indent
        for indent in verc_json["data"]["text"]
        if "text.element.Indent" in indent["class"]
    ]
    chunks = [
        chunk for chunk in verc_json["data"]["text"] if "text.chunk" in chunk["class"]
    ]

    # сделаем мап uid -> chunk
    uid_to_chunk = collections.OrderedDict(
        (str(uuid.UUID(c["uid"])), c) for c in chunks
    )

    # оборачиваем мап uid -> index в index -> uid
    chunk_index_to_uid = collections.OrderedDict(
        (chunk_index, str(uuid.UUID(uid)))
        for uid, chunk_index in verc_json["data"]["indexMap"].items()
    )

    # генератор текстовых значений чанков абзаца
    def chunk_text_values(indent):
        for index in indent["chunks"]:
            if "Varchar" in uid_to_chunk[chunk_index_to_uid[index]]["class"]:
                yield uid_to_chunk[chunk_index_to_uid[index]]["value"]

    # собираем результат uid абзаца -> его текст строкой

    indent_to_text = collections.OrderedDict(
        (
            str(uuid.UUID(indent["uid"])),
            reduce(lambda i, c: i + c, chunk_text_values(indent), ""),
        )
        for indent in indents
    )

    # фильтруем пустые, как непригодные для обработки
    indent_to_text = collections.OrderedDict(
        [non_empty for non_empty in indent_to_text.items() if non_empty[1] != ""]
    )
    return indent_to_text


# test
if __name__ == "__main__":

    with open("/home/argabidullin/ner_service/data/1.json", "r") as source:
        text = json.load(source)

    parsed_verc = read_verc(text)
    json.dump(parsed_verc, open("/home/argabidullin/ner_service/data/test.json", "w"))
