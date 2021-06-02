import nltk
import pymorphy2
import sklearn_crfsuite


def sentence_to_POS(sent: str, analyzer: pymorphy2.MorphAnalyzer):
    """ Преобразует предложение в POS формат (формат данных для предсказания) """

    token2POS = list()
    tokens = nltk.tokenize.word_tokenize(sent)

    for token in tokens:
        pos_tag = analyzer.parse(token)[0].tag.POS
        token2POS.append((token, pos_tag))

    return token2POS


def word_to_features(sent, i):
    """ Преобразует каждый токен в словарь признаков для CRF """

    word = sent[i][0]
    postag = sent[i][1]
    if postag is None:
        postag = "Fp"

    features = {
        "bias": 1.0,
        "word.lower()": word.lower(),
        "word[-3:]": word[-3:],
        "word.isupper()": word.isupper(),
        "word.istitle()": word.istitle(),
        "word.isdigit()": word.isdigit(),
        "postag": postag,
        "postag[:2]": postag[:2],
    }
    if i > 0:
        word1 = sent[i - 1][0]
        postag1 = sent[i - 1][1]
        if postag1 is None:
            postag1 = "Fp"
        features.update(
            {
                "-1:word.lower()": word1.lower(),
                "-1:word.istitle()": word1.istitle(),
                "-1:word.isupper()": word1.isupper(),
                "-1:postag": postag1,
                "-1:postag[:2]": postag1[:2],
            }
        )
    else:
        features["BOS"] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        postag1 = sent[i + 1][1]
        if postag1 is None:
            postag1 = "Fp"
        features.update(
            {
                "+1:word.lower()": word1.lower(),
                "+1:word.istitle()": word1.istitle(),
                "+1:word.isupper()": word1.isupper(),
                "+1:postag": postag1,
                "+1:postag[:2]": postag1[:2],
            }
        )
    else:
        features["EOS"] = True

    return features


def sent_to_features(sent):
    return [word_to_features(sent, i) for i in range(len(sent))]


def process_sentence(
    sent, analyzer: pymorphy2.MorphAnalyzer, model: sklearn_crfsuite.CRF
):
    """ Обрабатывает предложение и возвращает словарь token -> entity """

    tokens = nltk.tokenize.word_tokenize(sent)
    formatted_sentence = sentence_to_POS(sent, analyzer)
    sentence_features = list()
    sentence_features.append(sent_to_features(formatted_sentence))
    entities = model.predict(sentence_features)[0]

    token_to_entity: dict = {}
    for token, entity in zip(tokens, entities):
        print(token)
        token_to_entity[token] = entity

    return token_to_entity
