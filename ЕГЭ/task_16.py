# import sys
#
#
# sys.setrecursionlimit(3000)
#
#
# def f(n):
#     # return n if n < 11 else n + f(n - 1)
#     if n < 11:
#         return n
#     return n + f(n - 1)
#
#
# print(f(2024) - f(2021))

f_list = [0, 1, 2, 3, 4]


def f(n):
    if n > len(f_list):
        for i in range(len(f_list), n + 1):
            f_list.append(2 * i * f(i - 4))
    return f_list[n]


print((f(13766) - 9 * f(13762)) / f(13758))

