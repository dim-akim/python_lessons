"""
1 шаг. Запуск простейшего сервера на Flask

Этапы:

Импорт основного класса.

Создание экземпляра класса.

Декоратор, в котором описан путь. По этому URL будет обращаться пользователь.

Функция представления, которая вызывается при обращении пользователя к пути, указанному в декораторе.
"""

from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


# TODO вместо словаря вернуть HTML код
@app.route('/status')
def status():
    return {
        'status': 'OK',
        'name': 'Day-1-Messenger',
        'time': time.ctime(time.time())
    }


if __name__ == '__main__':
    app.run()
