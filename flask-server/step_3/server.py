"""
3 шаг. Использование шаблонов
В качестве шаблонов используем "Сайт начинающего верстальщика", который сделали на курсе "Основы HTML" в htmlacademy.
Шаблон - файл HTML

Этапы:

Импорт функции для отрисовки шаблона

Изменение функции index() - вместо текста возвращаем результат вызова функции отрисовки шаблона.
Первым параметром должно быть название файла шаблона - index.html.
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
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
