
database = {
    'Jack': 'Black',
    '1': '2',
    '3': '4'
}

login = 'Jack'


def check_password(login, password):
    if login in database:
        if database[login] == password:
            print('Ok', password)
            return True
        else:
            print('Bad password', password)
    elif login.lower() in database:
        print('Bad login - bad case', password)
    else:
        print('Bad login', password)
    return False


passwords = ['1', '2', 'black', 'Black', '3']
for p in passwords:
    print(check_password(login, p))


print('-' * 100)

i = 0
while i < len(passwords):
    print(check_password(login, passwords[i]))
    i += 1
