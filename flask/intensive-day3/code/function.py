
database = {
    'Jack': 'Black',
    '1': '2',
    '3': '4'
}


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
