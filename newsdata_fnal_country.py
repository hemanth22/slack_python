import requests
import os

NEWS_DATA_API = os.environ.get('NEWS_DATA_API')
#query = 'INR'

#url = 'https://newsdata.io/api/1/news?country=in&apikey='+NEWS_DATA_API

base_url = 'https://newsdata.io/api/1/news'

queries = ['fr','cn','sg','hk','in']

payload = {}
Healders = {}

for query in queries:
    parameters = {
        'country': query,
        'apiKey': NEWS_DATA_API
    }

    try:
        response = requests.request("GET", base_url, params=parameters, data=payload)
        if response.status_code == 200:
            news_data = response.json()
            if 'results' in news_data:
                results = news_data['results']
                for result in results:
                    html_format = '<a href="{}" target="_blank">{}</a>'.format(result['link'], result['title'])
                    print(result['description'],'|',result['content'],'|',result['source_id'],'|' , html_format)
    
                #for result in results:
                #    print("Title: ", result['title'])
                #    print("URL: ", result['link'])
                #    print("Description: ", result['description'])
                #    print("Content: ", result['content'])
                #    print("Source: ", result['source_id'])
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")