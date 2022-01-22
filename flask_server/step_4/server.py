"""
4 шаг. Исправляем ссылки на .css и картинки
Структура репозитория проекта на Flask:
    static/
        img/
        files/
    templates/
        *.html
    server.py

ПРОБЛЕМА:

Не подргружаются стили и картинки

Этапы решения:

Для файла index.html:
    Корректируем ссылку на файл стилей (6 строка): style.css -> static/style.css
    Корректируем ссылку на аватарку (13 строка): img/raccoon.svg -> static/img/raccoon.svg
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return f'''Hello, World!
    <br>
    <a href="index">index</a>'''


@app.route('/index')
def index():
    user = {'nickname': 'dim-akim'}

    return render_template('index.html', **user)


if __name__ == '__main__':
    app.run()
