import requests

# Replace 'YOUR_API_KEY' and 'API_ENDPOINT' with the actual API key and endpoint
api_key = 'NEWS_DATA_API'
api_endpoint = 'https://newsdata.io/api/1/news'

# Define any parameters required by the API
params = {
    'q': 'INR'
    # Add more parameters as needed
}

try:
    # Send an HTTP GET request to the API
    response = requests.get(api_endpoint, params=params, headers={'Authorization': api_key})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()

        # Process and display the news data as needed
        for idx, article in enumerate(news_data['articles'], start=1):
            print(f"Article {idx}:")
            print(f"Title: {article['title']}")
            print(f"Source: {article['source']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("\n")
    else:
        print(f"Request failed with status code {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
