import os
import typing as t

import dotenv
import pydantic
from typing_extensions import Literal

LISTEN_PATTERN = r"([0-9]{1,3}.){3}[0-9]{1,3}:[0-9]{2,5}"


class Config(pydantic.BaseModel):
    """ Модель данных конфигурации """

    listen: str = pydantic.Field(regex=LISTEN_PATTERN)
    debug: t.Optional[bool] = False
    development: t.Optional[bool] = False
    log_level: t.Optional[
        Literal["debug", "info", "warning", "error", "critical"]
    ] = "info"

    @pydantic.validator("log_level")
    def set_log_level(cls, level):
        return level or "info"


def read_config(config_file: str = ".env") -> Config:
    """ Читает конфигурационный файл и возвращает словарь """

    dotenv.load_dotenv(dotenv_path=config_file)

    raw_dict = {
        "listen": os.getenv("LISTEN"),
        "debug": os.getenv("DEBUG"),
        "development": os.getenv("DEVELOPMENT"),
        "log_level": os.getenv("LOG_LEVEL"),
    }
    return Config(**raw_dict)
