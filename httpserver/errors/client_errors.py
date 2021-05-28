from .error import Error

# Clients errors constants
CLIENT_REQUEST_FAILURE_ERROR_TYPE = "request/failed"
CLIENT_REQUEST_FAILURE_ERROR_UNKNOWN_REASON = "Unknown Reason"


# Bad request error constants
CLIENT_BAD_REQUEST_ERROR_TYPE = "client/bad-request"
CLIENT_BAD_REQUEST_STATUS_CODE = 400


# Resource not found error constants
CLIENT_NOT_FOUND_ERROR_TYPE = "client/not-found"
CLIENT_NOT_FOUND_ERROR_STATUS_CODE = 404


# Data conflict error constants
CLIENT_CONFLICT_ERROR_TYPE = "client/conflict"
CLIENT_CONFLICT_STATUS_CODE = 409


class ClientError(Error):
    """broad client errors class: 4--"""


class ClientBadRequestError(ClientError):
    """bad request: 400"""

    def __init__(self, *args, **kwargs):
        ClientError.__init__(
            self,
            *args,
            **kwargs,
            type_=CLIENT_BAD_REQUEST_ERROR_TYPE,
            status=CLIENT_BAD_REQUEST_STATUS_CODE,
        )


class ClientNotFoundError(ClientError):
    """resource not found: 404"""

    def __init__(self, *args, **kwargs):
        ClientError.__init__(
            self,
            *args,
            **kwargs,
            type_=CLIENT_NOT_FOUND_ERROR_TYPE,
            status=CLIENT_NOT_FOUND_ERROR_STATUS_CODE,
        )


class ClientConflictError(ClientError):
    """ conflict error: 409 """

    def __init__(self, *args, **kwargs):
        ClientError.__init__(
            self,
            *args,
            **kwargs,
            type_=CLIENT_CONFLICT_ERROR_TYPE,
            status=CLIENT_CONFLICT_STATUS_CODE,
        )
