import requests


api_url = 'http://numbersapi.com/{}/math'

params = {
    'json': 'true'
}
with open('dataset_24476_3.txt') as file:
    numbers = [int(line) for line in file]

for number in numbers:
    response = requests.get(api_url.format(number), params=params)
    if response.json()['found']:
        print('Interesting')
    else:
        print('Boring')
