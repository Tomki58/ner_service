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


# async def add_fact_type(request):
#     """Add user fact data view."""

#     data = await request.json()

#     try:
#         tomita_add_user_fact(data)
#     except (server_errors.ServerError, client_errors.ClientError) as err:
#         msg = serialize_error(err)
#         return http_error(status=err.status, errors=msg)
#     except confighdl.FactFound:
#         return http_ok("Fact already exists")
#     except Exception as err:
#         return http_error(str(err))
#     else:
#         return http_ok("Fact successfully added")


# async def add_fact_keyword(request):
#     """Add user fact keyword data view."""

#     data = await request.json()

#     try:
#         tomita_add_keyword(data)
#     except (client_errors.ClientError, server_errors.ServerError) as err:
#         msg = serialize_error(err)
#         return http_error(status=err.status, errors=msg)
#     except handlers_errors.KeywordExistance:
#         return http_ok("Keyword already exists")
#     except Exception as err:
#         return http_error(str(err))
#     else:
#         return http_ok("Keyword successfully added")


# myTODO: add view for tagging words in sentence
from httpserver.responses.responses import http_ok


async def tag_sentence(request):
    """ Process sentences with tags """

    data = await request.json()
    return http_ok("Success")

    # myTODO: implement function with tagging via tf2
