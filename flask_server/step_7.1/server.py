"""
Шаг 7.1. Больше изменяемых блоков в базовом шаблоне

Больше изменяемых блоков в шаблоне дает возможность более гибко настраивать каждую страницу.
В нашем шаблоне можно выделить:
    блок head - служебная информация для подключения стилей и т.п. внутри тега head
    блок header - заголовок страницы (для добавления дополнительных элементов) внутри тега header
    блок content - основное содержимое страницы внутри тега main
    блок footer - подвал сайта внутри тега footer

Отдельно можно заметить, что на страницах day-1, day-2, ..., day-15 есть повторяющийся элемент - ссылка "на главную"
Напрашивается еще один блок nav

Этапы:

Оборачиваем в базовом шаблоне содержимое тегов head, header и footer в изменяемые блоки языка Jinja2.

Добавляем в раздел header блок nav с тегом nav из day-1.

Превращаем все страницы day- и photo- в шаблоны, убирая всю лишнюю информацию, кроме содержимого тега main

На страницах photo- блок nav должен быть переопределен ссылкой на day-15
На странице start блок nav должен быть переопределен пустотой
"""

from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
Ссылка на <a href={url_for('base')}>базовую</a> страницу<br>
Ссылка на <a href={url_for('start')}>стартовую</a> страницу<br>
Ссылка на <a href={url_for('index')}>index</a> страницу<br>
"""


@app.route('/index')
def index():
    username = 'dim-akim'
    return render_template('index.html', username=username)


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/start')
def start():
    return render_template('start.html')


if __name__ == '__main__':
    app.run(debug=True)
