import pickle

import pymorphy2
import sklearn_crfsuite

from common.texthandlers import text_to_format
from httpserver.errors import client_errors, server_errors, transport_errors
from httpserver.workers.sentencedetector import detect
from httpserver.workers.sentenceprocessor import process_sentence


async def tagging(payload):
    """ Tag words in sentence """

    try:
        # map_: dict = payload["data"]
        file_path: str = payload["source"]
        map_ = text_to_format(file_path)
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

    crf_model: sklearn_crfsuite.CRF
    with open("./models/model", "rb") as source:
        crf_model = pickle.load(source)

    analyzer = pymorphy2.MorphAnalyzer(lang="ru")
    result = list()

    for sent in sentences:
        result.append(process_sentence(sent, analyzer, crf_model))

    return result
