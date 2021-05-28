import http
import traceback
from typing import Optional


class Error(Exception):
    def __init__(
        self,
        detail: Optional[str] = None,
        instance: Optional[str] = None,
        status: Optional[int] = None,
        title: Optional[str] = None,
        type_: Optional[str] = None,
    ):
        self.detail = detail
        self.instance = instance
        self.status = status or 500
        self.title = title or http.HTTPStatus(self.status).phrase
        self.type = type_

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: " + str(self.detail)

    def __repr__(self):
        tb = None
        if hasattr(self, "__traceback__") and self.__traceback__:
            tb = self.__traceback__
        return " ".join(traceback.format_exception(type(self), self, tb))
