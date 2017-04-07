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
    resp = sc.api_call(
        'files.upload',
        channel='#general',
        file=open('sample.txt').read(),
        title='sample.txt',
        channels='#general',
    )

    print(resp)


if __name__ == '__main__':
    cli()
