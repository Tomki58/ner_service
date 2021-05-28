import json
import uuid
import datetime
import traceback
from types import TracebackType

__all__ = ("json_dumps", "json_dump_traceback")


def json_dumps(data) -> str:
    """Dumps data to json with custom JSONEncoder."""
    return json.dumps(data, ensure_ascii=False, cls=JSONEncoder)


def json_dump_traceback(tb: TracebackType) -> str:
    """Dumps traceback to json as list of lines."""
    return json.dumps(traceback.format_tb(tb))


class JSONEncoder(json.JSONEncoder):
    """JSON encoder with datetime and UUID support."""

    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, uuid.UUID):
            return obj.hex
        elif isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
