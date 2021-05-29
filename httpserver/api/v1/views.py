# myTODO: delete all the views
# from pyservicetools.http.shortcuts import http_error, http_ok


# async def extract(request):
#     """Extract data view."""

#     data = await request.json()

#     try:
#         indent_to_xml = await tomita_extractor(data)
#     except (client_errors.ClientError, server_errors.ServerError) as err:
#         msg = serialize_error(err)
#         return http_error(status=err.status, errors=msg)
#     except Exception as err:
#         return http_error(str(err))
#     else:
#         result = transformers.tomita_xml_to_facts(indent_to_xml)
#         return http_ok(result)

from httpserver.errors import client_errors, server_errors, transport_errors
from httpserver.responses.responses import http_error, http_ok
from httpserver.workers.tagging import tagging
from helpers.serializers import serialize_error


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
