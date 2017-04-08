import json
import re
import os
import sys

import click
from logbook import Logger, StreamHandler
import requests
from slackclient import SlackClient


StreamHandler(sys.stderr).push_application()
log = Logger(__name__)

slack_token = os.environ['SLACK_API_TOKEN']
sc = SlackClient(slack_token)


def handle(event, context):
    handle_sns_topic(event)


def handle_ses_event(event):
    # for record in event['Records']:
    #     print(record['ses']['mail'])
    raise NotImplementedError()


def handle_sns_topic(event):
    for record in event['Records']:
        message = json.loads(record['Sns']['Message'])
        raw_content = message['content']
        headers, content = raw_content.split('\r\n\r\n', 1)

        # Looks like =\r\n is inserted into the message body...
        content = content.replace('=\r\n', '')

        urls = extract_attachment_hrefs(content)
        log.info('Found URLs = {}', urls)
        log.info('SLACK_API_TOKEN = {}', slack_token)
        for title, content in fetch_attachments(urls):
            print(title)
            resp = upload_to_slack(title, content)

            # TODO: Replace this with an appropriate logging library
            print(resp)


def extract_attachment_hrefs(content):
    return re.findall(
        r'https://www.miraeassetdaewoo.com/bbs/maildownload/[0-9_]+', content)


def fetch_attachments(urls):
    for url in urls:
        log.info('Fetching {}...', url)
        headers = {
            'Accept-Language': 'ko',
        }
        resp = requests.get(url, headers=headers)
        content_disp = resp.headers['Content-disposition']
        title = content_disp[len('Filename='):]

        yield title, resp.content


def upload_to_slack(title, content):
    log.info('Uploading to Slack ({} bytes)...', len(content))
    resp = sc.api_call(
        'files.upload',
        channel='#general',
        file=content,
        title=title,
        channels='#general',
    )

    return resp


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
def run(filename):
    with open(filename) as fin:
        content = fin.read()
        urls = extract_attachment_hrefs(content)
        for title, content in fetch_attachments(urls):
            resp = upload_to_slack(title, content)

            # TODO: Replace this with an appropriate logging library
            print(resp)


if __name__ == '__main__':
    cli()
