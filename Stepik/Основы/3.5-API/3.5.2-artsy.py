import requests


params = {
    'client_id': '77e60dfa6eb2370648ec',
    'client_secret': '5f8f718ba4d6e3f7e7c924093482a8f3'
}
artist_url = 'https://api.artsy.net/api/artists/'
token_url = f'https://api.artsy.net/api/tokens/xapp_token'

resp = requests.post(token_url, params=params)
token = resp.json()['token']
headers = {'X-Xapp-Token': token}
artists = []

with open('dataset_24476_4.txt') as file:
    for line in file:
        line = line.strip()
        response = requests.get(artist_url + line, headers=headers)
        response = response.json()
        artists.append((response['birthday'], response['sortable_name']))

for artist in sorted(artists):
    print(artist[1])
