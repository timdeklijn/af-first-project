import logging

import click

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.DEBUG)


@click.group()
def cli():
    pass


@cli.command(help="Ingest data into cronus-data")
def ingest():
    logger.info("ingesting data")


if __name__ == "__main__":
    cli()
