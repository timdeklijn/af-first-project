import logging

import click

from first_project.calc import do_calc

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.DEBUG)


@click.group()
def cli():
    pass


@cli.command(help="Ingest data into cronus-data")
def ingest():
    logger.info("ingesting data")


@cli.command(help="Do a complicated calculation")
@click.option("--num", help="number to fil a 10x10 array with", default=1)
@click.option("--fac", help="number to multiply array with", default=2)
def calc_it(num, fac):
    logger.info("doing a complicated calculation")
    result = do_calc(num, fac)
    logger.info(f"calculation finished with: {result}")


if __name__ == "__main__":
    cli()
