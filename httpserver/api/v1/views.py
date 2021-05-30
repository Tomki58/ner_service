from helpers.serializers import serialize_error
from httpserver.errors import client_errors, server_errors, transport_errors
from httpserver.responses.responses import http_error, http_ok
from httpserver.workers.tagging import tagging


async def tag_sentence(request):
    """ Process sentences with tags """

    data = await request.json()
    try:
        result = await tagging(data)
    except (
        client_errors.ClientError,
        server_errors.ServerError,
        transport_errors.TransportNoResponseError,
    ) as err:
        msg = serialize_error(err)
        return http_error(status=err.status, errors=msg)
    else:
        return http_ok(result)
