import requests


from_source = 'http://1060.ru'

response = requests.get(from_source)

print(response.headers)
print(response.text)
