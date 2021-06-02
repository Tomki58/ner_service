import uuid


def text_to_format(file_path: str):
    """ Разбивает сплошной текст на абзацы и превращает в словарь uuid -> предложения """

    uuid_text: dict = {}

    with open(file_path, "r") as source:
        for line in source:
            uuid_text[str(uuid.uuid4())] = line.strip()

    return uuid_text