import json


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
        headers, content = raw_content.split('\r\n\r\n', 2)

        extract_attachment_hrefs(content)


def extract_attachment_hrefs(content):
    pass
