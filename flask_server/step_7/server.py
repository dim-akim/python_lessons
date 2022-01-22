"""
Шаг 7. Выделение базового шаблона

Смысл использования шаблонизатора заключается в том, чтобы повторяющиеся куски разных страниц можно выделить
в отдельный шаблон, а в остальных файлах описывать не всю страницу целиком, а только изменяющуюся часть.

Базовый шаблон будет состоять из заголовка "Сайт начинающего верстальщика" и аватарки, а так же подвала сайта.
Блок <main></main> будет переопределяться

Этапы решения:

Делаем копию файла index.html и называем ее base.html

Тег с аватаркой <img class="avatar" ...> переносим из тега main в тег header

Все, что внутри тега main, удаляем, вместо этого обозначаем переопределяемый блок content

Создаем файл start.html и в первой строчке указываем, что он расширяет базовый шаблон base.html

Переопределяем блок content содержимым тега main из index.html (без аватарки)

Создаем на сервере два пути - /base и /start, функции представления которых возвращают соответствующие шаблоны

В функции hello дописываем ссылки на /base и /start с помощью url_for
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
