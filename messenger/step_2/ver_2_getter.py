"""
Простой получатель сообщений

Используем библиотеку requests и обращаемся методом GET по адресу http://127.0.0.1:5000/, записываем ответ в response
Посмотреть на разные поля:
    response.status_code
    response.headers
    response.text

Что такое JSON и чем он отличается от словаря Python?
    JSON - это универсальный способ указания словаря, который понимает любой язык программирования
    Отличия:
        всегда двойные кавычки
        True и False с маленькой буквы
        вместо None пишется null

Если обратиться по адресу http://127.0.0.1:5000/get_messages, в response.text будет просто текст
response.json() превращает его обратно в словарь Python, теперь можно обратиться по ключевым полям
в частности, в поле 'messages' лежит наш список сообщений, по нему можно проитерировать

"""


import requests
import time


while True:
    response = requests.get('http://127.0.0.1:5000/get_messages')
    answer = response.json()
    messages = answer['messages']

    for message in messages:
        print(message['username'])
        print(message['text'])
        print()

    time.sleep(.1)
