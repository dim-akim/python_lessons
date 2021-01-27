"""

"""

from flask import Flask, render_template, request
import time

server = Flask(__name__)

messages = [
    {'username': 'dim-akim', 'text': 'Здравствуйте!', 'timestamp': time.time()},
    {'username': 'fomin-k', 'text': 'Добрый день!', 'timestamp': time.time()},
    {'username': 'kaleda-s', 'text': 'И вам не хворать!', 'timestamp': time.time()}
]


@server.route('/')  # декоратор, который назначает путь
def hello():  # функция представления
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


# Добавить новый файл для отправки запросов и чтения ответов
# Нужна библиотека requests
@server.route('/get_messages')
def get_messages():
    after = float(request.args['after'])

    result = []
    for message in messages:
        if message['timestamp'] > after:
            result.append(message)
    return {
        'messages': result
    }


@server.route('/send_message')
def send_message():

    messages.append(
        {
            'username': request.json['username'],
            'text': request.json['text'],
            'timestamp': time.time()
        }
    )


@server.route('/index')
def index():  # функция представления
    name = 'Дмитрий Валерьевич'
    return render_template('index.html')


@server.route('/day-<num>')  # num - переменная
def day(num):  # функция представления
    return render_template(f'day-{num}.html')


server.run()  # Ctrl + Shift + F10
