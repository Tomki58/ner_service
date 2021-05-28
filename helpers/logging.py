import logging
import sys

import structlog

__all__ = ("init_logger",)

LEVELS = {"info": logging.INFO, "debug": logging.DEBUG}


def init_logger(level: str, format: str) -> logging.Logger:
    """Returns struct logger."""
    level = LEVELS.get(level, logging.INFO)
    setup_basic_logger(level)

    if format == "logfmt":
        ConsoleRenderer = structlog.dev.ConsoleRenderer
        renderer = ConsoleRenderer(
            level_styles=ConsoleRenderer.get_default_level_styles()
        )
    else:
        renderer = structlog.processors.JSONRenderer()
    processors = [
        structlog.stdlib.filter_by_level,  # включить фильтрацию по уровню
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,  # добавить уровень логирования
        structlog.processors.StackInfoRenderer(),  # рендерить стейктрейсы
        structlog.processors.format_exc_info,  # форматировать exc_info
        structlog.processors.UnicodeDecoder(),  # декодировать unicode
        renderer,
    ]
    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    return structlog.get_logger()


# TODO: move to setup_basic:
# from pyservicetools import logger
# logger.setup_basic()
def setup_basic_logger(level: int = logging.INFO) -> None:
    """Init basic app logger.

    Базовый конфиг логера, нужен для вывода в stdout и корректного вывода сообщений structlog.
    """
    logging.basicConfig(format="%(message)s", stream=sys.stdout, level=level)
