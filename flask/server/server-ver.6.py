"""
6 шаг. Использование форм

"""

from flask import Flask, flash, render_template, redirect
from forms import LoginForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/index')
def home():
    """
    Формирует домашнюю страницу
    Для тестирования генерирует поддельные объекты user и posts
    """
    title = 'Главная страница'
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('home.html', user=user, posts=posts, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Показывает страницу /login
    Если отправлена заполненная форма, перенаправляет на /index
    """
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title=form.title, form=form)


if __name__ == '__main__':
    app.run()
