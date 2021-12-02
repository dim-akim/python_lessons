"""
6 шаг. Использование динамического создания ссылок
TODO прочитать и разобраться
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
