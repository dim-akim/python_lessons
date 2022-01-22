"""
5 шаг. Использование переменных в URL

ПРОБЛЕМА:

Есть страницы day-1.html, day-2.html, ... , day-15.html. Создавать уникальный путь каждому - трудоемко.

Этапы решения:

Декоратор для нового пути /day-<num>. num - переменная (можно задавать ограничения по типу).

Функция представления day(num). num - та же самая переменная

Внутри функции передаем рендеру шаблонов название файла с помощью форматированной строки f'day-{num}.html'

В каждом шаблоне теперь надо скорректироввать ссылки на страницы
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


@app.route('/day-<num>')  # все, что находится в ссылке после 'day-', попадает в переменную num
def day(num):  # берем переменную num из декоратора пути
    return render_template(f'day-{num}.html')


if __name__ == '__main__':
    app.run()
