from .error import Error

# Transport error constants
TRANSPORT_NO_RESPONSE_ERROR_TYPE = "transport/no-response"
TRANSPORT_NO_RESPONSE_STATUS_CODE = 504


class TransportNoResponseError(Error):
    """broad transport errors class = 504"""

    def __init__(self, *args, **kwargs):
        Error.__init__(
            self,
            *args,
            **kwargs,
            type_=TRANSPORT_NO_RESPONSE_ERROR_TYPE,
            status=TRANSPORT_NO_RESPONSE_STATUS_CODE
        )
