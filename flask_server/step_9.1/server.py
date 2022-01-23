"""
Шаг 9.1 Оформление мгновенных сообщений

Первичное оформление мгновенных сообщений можно делать по классу flash контейнера div, которое содержит сообщение

Можно добавить дополнительный класс содержимому, взяв его из категории мгновенного сообщения

Этапы:

В функции form внутри мгновенного сообщения задать дополнительный параметр category:
    success для сообщения об удачном обращении
    error для сообщения об ошибке

В шаблоне формы внутри цикла из get_flashed_messages теперь берем кортеж категория, сообщение (cat, msg)
В самой функции get_flashed_messages должен появиться параметр True, который позволяет брать категорию сообщения

В контейнере div для мгновенного сообщения, помимо класса flash, указываем дополнительно класс из переменной cat

В файле стилей для формы указать настройки для классов flash, flash.success и flash.error. Например:

.flash {
  box-sizing: border-box;
  width: 630px;
  padding: 10px 390px 10px 10px;
}

.flash.success {
  border: 2px solid #8d745a;
  background: #47bb52;
}

.flash.error {
  border: 2px solid #ff0000;
  background: #ff7700;
}
"""

from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfgasgasdknasldfkhasodinfanwetiahsdovipans'


@app.route('/')
def hello():
    return f"""
Ссылка на <a href={url_for('base')}>базовую</a> страницу<br>
Ссылка на <a href={url_for('start')}>стартовую</a> страницу<br>
Ссылка на <a href={url_for('index')}>index</a> страницу<br>
Ссылка на <a href={url_for('form')}>страницу с формой</a>
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


if __name__ == '__main__':
    app.run(debug=True)
