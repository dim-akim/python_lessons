import requests


from_source = 'https://yandex.ru/search/?text=школа+1060'

response = requests.get(from_source)

print(response.content)
