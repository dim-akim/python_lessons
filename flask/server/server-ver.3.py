from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


@app.route('/index')
def index():
    user = {'nickname': 'Арсений'}  # выдуманный пользователь
    return render_template('index.html', **user)  # nickname='Арсений'


if __name__ == '__main__':
    app.run()