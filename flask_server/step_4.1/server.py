"""
4.1 шаг. Использование шаблонов (вставляем значение в шаблон)
Шаблон - файл HTML с динамическими параметрами.
Язык шаблонирования - Jinja2

Этапы:

Дополнительными параметрами могут выступать именованные значения (например, раскрытый словарь).

Например, чтобы параметр nickname отобразился на странице, в шаблоне он должен быть указан так: {{ nickname }}
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
    return render_template('index.html', nickname='Арсений')  # можно вставить nickname='Арсений'


if __name__ == '__main__':
    app.run()
