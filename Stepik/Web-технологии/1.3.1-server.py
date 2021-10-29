import requests


url = 'https://stepic.org/favicon.ico'

response = requests.get(url)
print(response.headers['Server'])
