from aiohttp import web

from common.logging import init_logger
from config import read_config
from httpserver.api.status.status import create_subapp as create_status_subapp
from httpserver.api.v1.routes import routes


async def create_app() -> web.Application:
    # app = web.Application(middlewares=(mdlwrs.traceid, mdlwrs.accesslog, mdlwrs.error))
    app = web.Application()
    for route in routes:
        method, url, view = route
        app.router.add_route(method, url, view)
    app.add_subapp("/status", create_status_subapp())
    app.cleanup_ctx.extend([setup_config, setup_logger, messenger])
    return app


async def setup_config(app):
    config = read_config()
    app["config"] = config
    yield
    pass


async def setup_logger(app):
    """Setups logger for app."""
    config = app["config"]
    level = "debug" if app["config"].debug is True else config.log_level
    format = "logfmt" if config.development is True else "json"
    log = init_logger(level, format)
    log.info("Log level setted", level=level)
    log.debug("Debug mode is ON")
    app["logger"] = log
    yield
    pass


async def messenger(app):
    log = app["logger"]
    log.info("Application started", listen=app["config"].listen)
    yield
    log.info("Shutting down application")
