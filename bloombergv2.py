import requests
import json
import os

BLOOM_KEY = os.environ.get('BLOOM_KEY')
BLOOM_HOST = os.environ.get('BLOOM_HOST')

url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

querystring = {"query":"SGD"}
#querystring = {"query":"INR"}

headers = {
        "X-RapidAPI-Key": BLOOM_KEY,
        "X-RapidAPI-Host": BLOOM_HOST
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

for value in data["news"]:
    print(value["title"],'|',value["card"])