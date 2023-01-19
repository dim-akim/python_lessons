import requests


source = 'http://1060.ru/'  # URL - Universal Resource Locator - ссылка на ресурс

response = requests.get(source)

print(response.text)
