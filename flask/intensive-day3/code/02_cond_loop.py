
database = {
    'Jack': 'Black',
    '1': '2',
    '3': '4'
}

login = 'Jack'
password = 'Black'

# if login in database:
#     if database[login] == password:
#         print('Ok')
#     else:
#         print('Bad password')
# elif login.lower() in database:
#     print('Bad login - bad case')
# else:
#     print('Bad login')

passwords = ['1', '2', 'black', 'Black', '3']
for p in passwords:
    print('trying', p)
    if database[login] == p:
        print(password)
        # break

i = 0
while i < len(passwords):
    print('trying', i)
    if database[login] == passwords[i]:
        print(password)
        break
    i += 1  # i = i + 1
