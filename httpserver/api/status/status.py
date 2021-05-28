import json

import structlog
from aiohttp import web
from httpserver.responses.responses import http_ok


async def ping(request):
    return http_ok({})


# myTODO: rewrite for simple usage without extractor
async def alive(request):
    # if EXTRACTOR.is_running:
    #     return http_ok({})
    # else:
    #     err = server_errors.BackendServerError(
    #         instance="GET /alive", detail="Extractor is not running"
    #     )
    #     return http_error(status=err.status, errors=serialize_error(err))
    return http_ok({})


async def version(request):
    with open("version.json") as info:
        return http_ok(json.loads(info.read()))


def create_subapp(logger=structlog.get_logger()):
    subapp = web.Application()
    subapp["logger"] = logger

    subapp.router.add_get("/ping", ping)
    subapp.router.add_get("/alive", alive)
    subapp.router.add_get("/version", version)
    return subapp
