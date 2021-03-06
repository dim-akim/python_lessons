"""
2 шаг. Функционал мессенджера

Этапы:

Функция отправки сообщений
Функция приема сообщений
Список всех сообщений
Словарь пользователей и паролей

Для работы с сервером нужны модули sender и getter
"""

from flask import Flask, request
from datetime import datetime
import time

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
messages = [
    {'username': 'Jack', 'text': 'Hello from Jack!', 'timestamp': time.time()},
    {'username': 'Nancy', 'text': 'Hello from Nancy!', 'timestamp': time.time()},
    {'username': 'Nancy', 'text': 'How are you?', 'timestamp': time.time()}
]

users = {
    'Jack': '12345',
    'Nancy': '12345'
}


@app.route('/')
def hello():
    return 'Привет! Ты на главной странице мессенджера. Его <a href="/status">статус</a>.'


@app.route('/status')
def status():
    return {
        'status': 'OK',
        'name': 'Day-1-Messenger',
        'server_start_time': server_start,
        'server_current_time': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),
        'current_time': time.time(),
        'messages': len(messages),
        'users': len(users)
    }


@app.route('/send_message')
def send_message():
    username = request.json['username']
    text = request.json['text']

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})

    return {'ok': True}


@app.route('/get_messages')
def get_message():
    after = float(request.args['after'])
    result = []
    for message in messages:
        if message['timestamp'] > after:
            result.append(message)

    return {
        'messages': result
    }


if __name__ == '__main__':
    app.run(debug=True)
