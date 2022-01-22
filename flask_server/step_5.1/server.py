"""
5.1 шаг. Использование переменных в URL

Повторяем создание пути и функции представления с переменной для страниц photo-1, photo-2 и photo-3
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


@app.route('/photo-<num>')  # все, что находится в ссылке после 'photo-', попадает в переменную num
def photo(num):  # берем переменную num из декоратора пути
    return render_template(f'photo-{num}.html')


if __name__ == '__main__':
    app.run()
