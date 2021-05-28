from httpserver.api.v1.views import tag_sentence

routes = (("post", "/api/v1/tag_sentence", tag_sentence),)
