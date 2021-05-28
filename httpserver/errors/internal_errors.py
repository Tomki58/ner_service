from .error import Error

EXTRACTOR_ERROR_TYPE = "extractor/error"


class ExtractorError(Error):
    """ broad extractor errors class """

    def __init__(self, *args, **kwargs):
        Error.__init__(self, *args, **kwargs, type_=EXTRACTOR_ERROR_TYPE)
