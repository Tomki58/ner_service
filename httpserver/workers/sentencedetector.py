import json
from json import decoder

import aiohttp
import structlog
from aiohttp import client_exceptions

from httpserver.errors import server_errors, transport_errors


async def detect(text, mode="sentences") -> dict:
    """
    :param text: текст для разбиения на предложения
    :param mode: тип возвращаемого значения "sentences" - вернет предложения, "positions" - вернет позиции
    """
    log = structlog.get_logger()

    url = "http://localhost:9010/api/v1/detect/"

    try:
        response = await aiohttp.ClientSession().post(
            url,
            json={"mode": mode, "source": text},
            headers={"content-type": "application/json"},
        )
    except client_exceptions.ClientConnectorError as connection_err:
        log.error(str(connection_err))
        err = transport_errors.TransportNoResponseError(
            detail=str(connection_err), instance="POST /detect/"
        )
        raise err

    try:
        response = await response.json()
        # Возвращаем словарь {uid абзаца -> [предложения]}
        return response["data"]
    except decoder.JSONDecodeError as json_error:
        log.error(str(json_error))
        err = server_errors.BackendServerError(
            detail="Invalid payload for sentence detector", instance="POST /detect/"
        )
        raise err
    except Exception as err:
        log.error(str(err))
        raise


import asyncio

if __name__ == "__main__":

    with open("/home/argabidullin/lingvo/data/test.json", "r") as source:
        text = json.load(source)
    print(text)

    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(detect(text))

    for indent in ret.values():
        print(len(indent))
