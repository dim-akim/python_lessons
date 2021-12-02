"""
2 шаг. Использование HTML

Этапы:

Декоратор для нового пути /index.

Функция представления index(). Функция возвращает HTML-код - текст с тегами.

В функции index() задан словарь, имитирующий данные о пользователе.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/index')
def index():
    user = {'nickname': 'Арсений'}  # выдуманный пользователь
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''    # возвращаем HTML-код


if __name__ == '__main__':
    app.run()
