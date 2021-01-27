import requests


# Создаем сообщение
username = input('Твое имя: ')

while True:
    text = input('Введи текст сообщения: ')

    # Запаковываем сообщение в GET-запрос
    requests.get(
        'http://127.0.0.1:5000/send_message',
        json={'username': username, 'text': text}
    )
