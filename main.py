import os

import click
from slackclient import SlackClient


slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)


@click.group()
def cli():
    pass


@cli.command()
def upload():
    raise NotImplementedError()


if __name__ == '__main__':
    cli()
