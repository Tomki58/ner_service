from httpserver.errors import client_errors, server_errors, transport_errors
from httpserver.workers.sentencedetector import detect


async def tagging(payload):
    """ Tag words in sentence """

    try:
        map_: dict = payload["data"]
    except:
        raise client_errors.ClientBadRequestError(
            detail="not found `data`", instance="POST /tag_sentence"
        )

    try:
        indent_to_sentences = await detect(map_)
    except (
        server_errors.ServerError,
        transport_errors.TransportNoResponseError,
    ) as detector_err:
        err = client_errors.ClientConflictError(
            detail=detector_err, instance="POST /extract"
        )
        raise err
    except:
        raise

    sentences = list()
    for _, sntns in indent_to_sentences.items():
        sentences.extend(sntns)

    return sentences
