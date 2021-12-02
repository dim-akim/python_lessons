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
    Корректируем ссылку на аватарку (15 строка): img/raccoon.svg -> static/img/raccoon.svg

Для всех остальных файлов:
    Корректируем ссылки на все статичные материалы (стили, картинки, файлы), добавляя префикс static/ в ссылку
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return f'''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


@app.route('/index')
def index():
    user = {'nickname': 'Арсений'}  # выдуманный пользователь

    # return render_template('index.html', **user)  # другой вариант передачи именованного параметра
    return render_template('index.html', nickname='Добрый вечер')  # можно вставить nickname='Арсений'


if __name__ == '__main__':
    app.run()
