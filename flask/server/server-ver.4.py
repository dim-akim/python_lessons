"""
4 шаг. Использование переменных в URL
В качестве шаблонов используем "Сайт начинающего верстальщика", который сделали на курсе "Основы HTML" в htmlacademy

Проблема:

Есть страницы day-1.html, day-2.html, ... , day-15.html. Создавать уникальный путь каждому - трудоемко.

Этапы:

Декоратор для нового пути /day-<num>. num - переменная (можно задавать ограничения по типу).

Функция представления day(num). num - та же самая переменная

Внутри функции передаем рендеру шаблонов название файла с помощью форматированной строки f''
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
    return render_template('index.html', **user)  # nickname='Арсений'


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


if __name__ == '__main__':
    app.run()
