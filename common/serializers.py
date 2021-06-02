from httpserver.errors.error import Error


def serialize_error(error: Error) -> dict:
    """ Сериализует ошибку в словарь """
    detail = (
        serialize_error(error.detail)
        if isinstance(error.detail, Error)
        else error.detail
    )
    return {
        "detail": detail,
        "instance": error.instance,
        "status": error.status,
        "title": error.title,
        "type": error.type,
    }
