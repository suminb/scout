(Unnamed Project)
---
TODO: Name this project as soon as possible.

The primary purpose of this project is to perform the following tasks:

1. Receive analyst reports via email every morning (AWS SES).
1. Extract PDF files (the actual reports).
1. Extract text from those files and summarize it (<http://tldr.kr>).
1. Upload the summary along with the original PDF to a private Slack channel.

Receiving emails with AWS SES
---

In order to receive email messages via AWS SES, a user-owned domain name must
be provided. Refer [this document](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-verification.html)
for more details.

I've set up a `TXT` record and an `MX` record on my domain, as directed in the
AWS console.

AWS Lambda
---
We use Apex in order to manage AWS Lambda functions.

* <http://apex.run>

Uploading files to a Slack channel
---

* <https://github.com/slackapi/python-slackclient>
* <https://api.slack.com/methods/files.upload>
* <https://api.slack.com/tokens>
