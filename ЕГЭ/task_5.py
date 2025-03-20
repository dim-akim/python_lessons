# r_numbers = []
# for n in range(4, 2000):
#     n2 = bin(n)[2:]
#     if n % 3 == 0:
#         n2 += n2[-3:]
#     else:
#         n2 += bin((n % 3) * 3)[2:]
#     r = int(n2, 2)
#     if r <= 170:
#         r_numbers.append(r)
#         print(f'{n=} {n2=} {r=}')
#
# print(sorted(r_numbers))

#
def to5(n: int):
    result = ''
    while n > 0:
        result = str(n % 5) + result
        n //= 5
    return result

for n in range(25, 27):
    n5 = to5(n)
    if n % 25 == 0:
        r5 = n5[-3:] + n5
    else:
        r5 = n5 + to5(n % 25)
    r = int(r5, 5)
    # if r > 10000:
    print(f'{n=} {n5=} {r5=} {r=}')

# for n in range(1, 10000):
#     string = ''
#     x = n
#     # print(f'{n=}')
#     while n > 0:
#         string += str(n % 5)
#         n //= 5
#
#     string = string[::-1]
#     # print(f'{string=}')
#     if int(string) % 25 == 0:
#         string += string[-3::]
#     else:
#         m_str = ''
#         m = int(string) % 25
#         while m > 0:
#             m_str += str(m % 5)
#             m //= 5
#         string += m_str[::-1]
#         # print(f'after {string=} {int(string, 5)} {x=}')
#     if int(string, 5) > 10000:
#         print(x)
