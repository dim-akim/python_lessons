"""
Получатель сообщений из мессенджера

Отправляет в запросе дополнительный параметр - last_timestamp - метка времени последнего сообщения
Получает только те сообщения, которые пришли позже метки

Сервер должен принять и обработать дополнительный запрос
"""

import requests
import time
from datetime import datetime

last_timestamp = 0.0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/get_messages',
        params={'after': last_timestamp}
    )
    messages = response.json()['messages']

    for message in messages:
        dt = datetime.fromtimestamp(message['timestamp'])
        dt = dt.strftime('%H:%M:%S %d/%m/%Y')
        print(dt, message['username'])
        print(message['text'])
        print()
        last_timestamp = message['timestamp']

    time.sleep(.01)
