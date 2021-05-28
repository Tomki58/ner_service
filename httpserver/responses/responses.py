"""
    HTTP response & errors shortcuts.
"""

from aiohttp import web

from helpers.json_encoder import json_dumps

__all__ = ("http_ok", "http_error")

HTTP_OK = web.HTTPOk.status_code
HTTP_BAD_REQUEST = web.HTTPBadRequest.status_code


def http_ok(data: object, status: int = HTTP_OK, errors: list = None) -> web.Response:
    """Positive HTTP response shortcut."""
    if errors is not None:
        if not isinstance(errors, list):
            errors = [errors]
    payload = {"success": True, "data": data, "errors": errors}
    return web.json_response(payload, status=status, dumps=json_dumps)


def http_error(status: int = HTTP_BAD_REQUEST, errors: list = None) -> web.Response:
    """Negative HTTP response shortcut."""
    if not isinstance(errors, list):
        errors = [errors]
    payload = {"success": False, "errors": errors, "data": None}
    return web.json_response(payload, status=status, dumps=json_dumps)
