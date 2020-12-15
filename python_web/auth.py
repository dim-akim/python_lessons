# Словарь - dictionary

database = {
    'dim-akim': 'abcdf',
    'FominK': 'blablabla',
    'Jack': 'Black',
    'Varya': 'f,hfrflf,hf'
}


def check_password(login, password):
    if login in database:
        if database[login] == password:
            return True
    return False


password_count = 0
user_login = 'dim-akim'

with open('pop-passwords.txt') as passwords_file:
    for line in passwords_file:
        user_password = line.strip()

        if check_password(user_login, user_password) is True:
            print(f'Попытка № {password_count}: пароль {user_password} подошел')
            break

        password_count += 1

print(f'файл закрыт, {password_count=}')
