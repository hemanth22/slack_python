import requests
import json
import os

IFTTT_WEBHOOK = os.environ.get('IFTTT_WEBHOOK')

base_url = f'https://maker.ifttt.com/trigger/bitroid_hello/with/key/{IFTTT_WEBHOOK}'

payload = {
    'value1': 'this is a remainder',
    'value2': 'to book a cab',
    'value3': 'for next week'
}

headers1 = {
  'Content-Type': 'application/json'
}

try:
    response = requests.post(base_url, json=payload)
    if response.status_code == 200:
        print('JSON payload sent successfully to IFTTT Webhook')
    else:
        print(f'Failed to send JSON payload. Status code: {response.status_code}')
except Exception as e:
    print(f'An error occurred: {str(e)}')