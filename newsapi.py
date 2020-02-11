import requests
import secrets

base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "country": "us",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
# print(result)
articles = result['articles']
for a in articles:
    print(a['title'], '-', a['source']['name'])