"""
Шаг 9. Мгновенные сообщения при отправке формы

ПРОБЛЕМА: при отправке формы происходит открытие той же самой страницы с пустой формой.
Непонятно, отправлена она или нет.

Чтобы пользователь мог получить реакцию на отправленную форму, существует механизм мгновенных сообщений.
Во Flask это реализовано с помощью функций flash (сторона приложения) и get_flashed_messages (сторона шаблона).
Они, соответственно, записывают и вынимают эти сообщения в специальный объект session, в котором хранится вся информация
о текущей сессии.

Т.е. при первом открытии формы никакого сообщения не будет, потом, например, при удачной отправке, функция flash
запишет сообщение в сессию, а функция get_flashed_messages возьмет его оттуда, и сообщение появится на странице.
При обновлении страницы оно опять пропадет, потому что никаких новых сообщений в session записано не будет

Этапы решения:

Импортируем функцию flash из пакета flask

В функции form добавляем проверку на длину полного имени (или любую другую) после проверки на метод запроса:
    если проверка пройдена, записываем мгновенное сообщение об успехе - flash('Обращение принято')
    если проверка НЕ пройдена, записываем мгновенное сообщение об отказе - flash('Вы допустили ошибку')
Проверку можно сделать более сложной и вынести в отдельную функцию. Действия по обработке запроса можно тоже выполнять
только после прохождения этой проверки.

В шаблоне формы form.html добавляем цикл с помощью языка Jinja2 непосредственно перед тегом form:
    {% for msg in get_flash_messages() %}
    <div class="flash">{{ msg }}</div>
    {% endfor %}
Этот цикл выведет все сообщения, которые хранятся в этот момент в session, и обернет каждое в тег div с классом flash

Провести проверку и прочитать ошибку про секретный ключ

Для работы session, куда отправляет мгновенные сообщения функция flash, нужно задать секретный ключ.
Это строка произвольной длины и случайного содержимого. Чем она длинее, тем сложнее будет расшифровать содержимое.

Сразу после создания приложения нужно написать следующую строчку app.config['SECRET_KEY'] = '<символы>'

ПРОВЕРКА: попробовать отправить форму, удовлетворяющую условию и неудовлетворяющую. Обновить страницу несколько раз.
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
            flash('Обращение принято')
        else:
            flash('Вы допустили ошибку')
        for item in request.form:
            print(item, request.form[item])
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
