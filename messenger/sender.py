import requests


username = input('Твое имя: ')

while True:
    text = input('Введи сообщение: ')

    requests.get(
        'http://127.0.0.1:5000/send_message',
        json={'username': username, 'text': text}
    )
