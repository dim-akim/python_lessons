"""
6 шаг. Использование динамического создания ссылок

ПРОБЛЕМА: если адрес главной страницы (/index) изменится (например, на /blog/index), ссылка в hello перестанет работать
Кроме того, она перестанет работать во всех шаблонах.
При каждом изменении ссылки на сервере изменять все шаблоны, в которых она могла встретиться, нерационально.

Этапы решения:

Импортируем функцию url_for из пакета flask

В функции hello заменяем простую ссылку (href="/index") на href="{url_for('index')}" (используем f-строку)

ПРОВЕРКА: изменить адрес в декораторе функции index и убедиться, что ссылка каждый раз работает
при изменении адреса в декораторе функции index может перестать работать ссылка на файл стилей.

Функцию url_for можно использовать не только в файлах .py, но и в шаблонах:

Корректируем ссылку на 6 строке: static/style.css -> {{ url_for('static', filename='style.css') }}

Корректируем ссылку на 15 строке: static/img/raccoon.svg -> {{ url_for('static', filename='img/raccoon.svg') }}

Корректируем ссылки на 19-33 строках: day-1 -> {{ url_for('day', num=1) }} и т.п.

ОСОБОЕ ВНИМАНИЕ уделяем файлам:
    day-15.html
    photo-1.html
    photo-2.html
    photo-3.html
"""

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def hello():
    return f'''Hello, World!
    <br>
    <a href="{url_for('index')}">index</a>'''  # было просто href="/index"


@app.route('/index')
def index():
    user = {'nickname': 'dim-akim'}
    return render_template('index.html', **user)


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


if __name__ == '__main__':
    app.run()
