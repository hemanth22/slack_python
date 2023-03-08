import json
import requests
import os

SLACK1=os.environ.get('SLACK1')
SLACK2=os.environ.get('SLACK2')
SLACK3=os.environ.get('SLACK3')

with open('bloombergv1news.txt','r') as file:
    file_contents = file.read()

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = 'https://hooks.slack.com/services/'+SLACK1+'/'+SLACK2+'/'+SLACK3

slack_data = {'text': file_contents}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )
