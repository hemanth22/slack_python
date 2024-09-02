import requests
import os
import json

NEWS_DATA_API = os.environ.get('NEWSDATA_API_KEY')

base_url = 'https://newsdata.io/api/1/news'
queries = ['fr', 'cn', 'sg', 'hk', 'in']

payload = {}
headers = {}

for query in queries:
    parameters = {
        'country': query,
        'apiKey': NEWS_DATA_API,
        'language': 'en'
    }

    try:
        response = requests.request("GET", base_url, params=parameters, data=payload)
        if response.status_code == 200:
            news_data = response.json()
            if 'results' in news_data:
                for result in news_data['results']:
                    formatted_json = {
                        "source": "news",
                        "message": {
                            "title": result.get('title', 'no news'),
                            "description": result.get('description', 'no news'),
                            "source_id": result.get('source_id', 'unknown')
                        }
                    }
                    formatted_output = json.dumps(formatted_json, indent=4)
                    print(formatted_output)
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
