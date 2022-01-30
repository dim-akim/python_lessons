"""
Шаг 10. Сценарий авторизации - форма, редирект

"""

from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfgasgasdknasldfkhasodinfanwetiahsdovipans'

users = [
    {'username': 'dim-akim', 'password': '12345', 'is_admin': True},
    {'username': 'Student', 'password': '1060', 'is_admin': False},
]

@app.route('/')
def hello():
    return f"""
Ссылка на <a href={url_for('base')}>базовую</a> страницу<br>
Ссылка на <a href={url_for('start')}>стартовую</a> страницу<br>
Ссылка на <a href={url_for('index')}>index</a> страницу<br>
Ссылка на <a href={url_for('form')}>страницу с формой</a><br>
Ссылка на <a href={url_for('login')}>страницу авторизации</a><br>
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


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if len(request.form['fullname']) > 2:
            flash('Обращение принято', category='success')
        else:
            flash('Вы допустили ошибку', category='error')
        for item in request.form:
            print(item, request.form[item])
    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if user['username'] == request.form['username']:
                if user['password'] == request.form['password']:
                    return redirect(url_for('profile', username=user['username']))
                else:
                    flash('Неверный пароль', category='error')
        flash('Нет такого пользователя', category='error')
    return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    return f'Вы находитесь в профиле {username}'


if __name__ == '__main__':
    app.run(debug=True)
