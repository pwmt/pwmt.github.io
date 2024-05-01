#!/usr/bin/python

import click
from pwmt import app, freezer

@click.group()
def cli():
    pass

@click.command()
def freeze():
    freezer.freeze()

@click.command()
def serve():
    app.run(host='0.0.0.0')

cli.add_command(freeze)
cli.add_command(serve)

if __name__ == "__main__":
    cli()
