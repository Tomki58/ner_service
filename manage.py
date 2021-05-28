import asyncio

import click
from aiohttp import web
from httpserver import app


@click.group()
def cli():
    pass


@cli.command()
def runserver():
    """ Запускает http сервер """
    from config import read_config

    config = read_config()
    host, port = config.listen.split(":")
    port = int(port)
    # Создание backup'a
    loop = asyncio.get_event_loop()
    application = loop.run_until_complete(app.create_app())

    web.run_app(application, host=host, port=port)


if __name__ == "__main__":
    try:
        cli()
    except Exception as err:
        print(str(err))
