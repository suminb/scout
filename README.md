(Unnamed Project)
---
TODO: Name this project as soon as possible.

The primary purpose of this project is to perform the following tasks:

1. Receive analyst reports via email every morning (AWS SES).
1. Extract PDF files (the actual reports).
1. Extract text from those files.
1. Upload the content to a private Slack channel.

Receiving Emails with AWS SES
---

In order to receive email messages via AWS SES, a user-owned domain name must
be provided. Refer [this document](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-verification.html)
for more details.

I've set up a `TXT` record and an `MX` record on my domain, as directed in the
AWS console.
