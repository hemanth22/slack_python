import os
import requests
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")



api_key =  os.environ.get('NEWS_API')
# Specify the base URL for the News API
base_url = 'https://newsapi.org/v2/'

# Define the endpoint you want to use, e.g., top headlines or everything
endpoint = 'top-headlines'
all_categories = ['business','entertainment','general','health','science','sports','technology']
# Specify the parameters for your request (e.g., country, category, sources, etc.)
for all_category in all_categories:
    print("News Category: ",f"{all_category}","\n")
    parameters = {
    'country': 'US',  # Replace with your desired country
    'category': all_category,  # Replace with your desired category
    'apiKey': api_key,
    }

    # Make the API request
    
    response = requests.get(f"{base_url}{endpoint}", params=parameters)

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

    # Check if there are articles in the response
        if 'articles' in data:
            articles = data['articles']


        # Print the headlines and descriptions of the articles
            for article in articles:
                html_format = '<a href="{}" target="_blank">{}</a>'.format(article["url"], article["title"])
                print(article['description'],'|',article['source']['name'],'|' , html_format)
#        for article in articles:
#            print("Title:", article['title'])
#            print("Description:", article['description'])
#            print("Source:", article['source']['name'])
#            print("URL:", article['url'])
#            print("\n")
            else:
                print("No articles found in the response.")
        else:
            print("Error:", response.status_code)
