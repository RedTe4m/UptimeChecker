

import requests
import json


webhook_url = 'https://hooks.slack.com/services/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'
slack_data = {'text': "Website down :spaghetti:"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
