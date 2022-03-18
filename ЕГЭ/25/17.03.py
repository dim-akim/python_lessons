# deliteli = []
#
# for number in range(174457, 174506):
#     for d in range(2, int(number**0.5) + 1):
#         if number % d == 0:
#             deliteli.append(d)
#             deliteli.append(number // d)
#         if len(deliteli) > 2:
#             break
#     if len(deliteli) == 2:
#         print(number, deliteli)
#     deliteli = []

def is_simple(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

n = 0
for number in range(5, 10):
    n += 1
    if is_simple(number):
        print(n, number)

