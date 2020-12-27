"""
3 шаг. Функционал мессенджера: отправка сообщений

Этапы:

Изменение структуры сообщения - добавляем поле для метки времени timestamp

Функция, которая принимает сообщение и записывает его в список messages, добавляя метку времени

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
        'messages': len(messages)
    }


@app.route('/send_message')
def send_message():
    username = request.json['username']
    text = request.json['text']

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})

    return {'ok': True}


@app.route('/get_messages')
def get_message():
    return {
        'messages': messages
    }


if __name__ == '__main__':
    app.run(debug=True)
