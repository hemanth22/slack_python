import requests
import os

# Replace 'YOUR_API_KEY' with your actual News API key
api_key =  os.environ.get('NEWS_API')

# Specify the base URL for the News API 
base_url = 'https://newsapi.org/v2/'

# Define the endpoint for the "everything" API
endpoint = 'everything'

# Define list of countries
queries = ['USD', 'SGD', 'INR']

for query in queries:
    print("News Country: ",f"{query}","\n")
    parameters = {
        'q': query,
        'apiKey': api_key,
    }

# Specify the parameters for your request (e.g., query, sources, date, etc.)
#parameters = {
#    'q': 'SGD',  # Replace with your desired query
#    'apiKey': api_key,
#}

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
