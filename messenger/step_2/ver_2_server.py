"""
2 шаг. Функционал мессенджера: хранение сообщений

Этапы:

Список всех сообщений, который хранит каждое сообщение в виде словаря
Функция, которая отдает все сообщения при запросе на адрес /get_messages

Для работы с сервером нужен модуль getter
"""

from flask import Flask, request
from datetime import datetime
import time


app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %d/%m/%Y')  # опционально
messages = [
    {'username': 'Jack', 'text': 'Hello from Jack!'},
    {'username': 'Nancy', 'text': 'Hello from Nancy!'},
    {'username': 'Nancy', 'text': 'How are you?'}
]


@app.route('/')
def hello():
    return 'Привет! Ты на главной странице мессенджера. Его <a href="/status">статус</a>.'


@app.route('/status')
def status():
    return {
        'status': 'OK',
        'name': 'Day-1-Messenger',
        'server_start_time': server_start,  # опционально
        'server_current_time': datetime.now().strftime('%H:%M:%S %d/%m/%Y'),  # опционально
        'messages': len(messages)
    }


@app.route('/get_messages')
def get_message():
    return {
        'messages': messages
    }


if __name__ == '__main__':
    app.run(debug=True)  # при фиксации изменений сервер перезапускается сам
