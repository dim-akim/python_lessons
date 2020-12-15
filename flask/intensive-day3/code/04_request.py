# from function import check_password
# import function
#
# login = 'Jack'
# passwords = ['1', '2', 'black', 'Black', '3']
#
# for p in passwords:
#     if function.check_password(login, p):
#         break
#
# print('-' * 100)
#
# i = 0
# while i < len(passwords):
#     if function.check_password(login, passwords[i]):
#         break
#     i += 1

# import json
#
# s = json.dumps({"name": True})
# print(s)

import requests

for i in range(1000):
    print(requests.post('http://127.0.0.1:5000/auth', json={'login': 'admin', 'password': '123456'}).status_code)
