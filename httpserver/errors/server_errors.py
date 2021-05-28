from .error import Error

# Internal server error constants
INTERNAL_SERVER_ERROR_TYPE = "server/internal-error"
INTERNAL_ERROR_STATUS_CODE = 500


# Bad gateway status code
BACKEND_BAD_GATEWAY_STATUS_CODE = 502

# Backend server error constants
BACKEND_SERVER_ERROR_TYPE = "backend/server-error"

# Backend bad response error constants
BACKEND_BAD_RESPONSE_TYPE = "backend/bad-response"


class ServerError(Error):
    """broad server errors class: 5--"""


class ServerInternalError(ServerError):
    """server internal error: 500"""

    def __init__(self, *args, **kwargs):
        ServerError.__init__(
            self,
            *args,
            **kwargs,
            type_=INTERNAL_SERVER_ERROR_TYPE,
            status=INTERNAL_ERROR_STATUS_CODE
        )


class BackendServerError(ServerError):
    """backend server error: 502"""

    def __init__(self, *args, **kwargs):
        ServerError.__init__(
            self,
            *args,
            **kwargs,
            type_=BACKEND_SERVER_ERROR_TYPE,
            status=BACKEND_BAD_GATEWAY_STATUS_CODE
        )


class BackendBadResponse(ServerError):
    """backend bad response: 502"""

    def __init__(self, *args, **kwargs):
        ServerError.__init__(
            self,
            *args,
            **kwargs,
            type_=BACKEND_BAD_RESPONSE_TYPE,
            status=BACKEND_BAD_GATEWAY_STATUS_CODE
        )
