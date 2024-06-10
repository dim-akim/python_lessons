def f7(n):
    if n < 3:
        return 1
    # result = 0
    # for i in range(1, n):
    #     result += f7(i)
    #
    # return result
    return sum(f7(i) for i in range(1, n))


def f8(n):
    if n >= len(f8_list):
        for i in range(len(f8_list), n + 1):
            f8_list.append(i + f8(i - 1))
    return f8_list[n]


def f10(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f10(n // 10) + n % 10
    return f10(n // 10)


f8_list = [10] * 11

# for i in range(1000):
#     print(i, f10(i))
#
# total = 0
# for a1 in '1':
#     for a2 in '013579':
#         for a3 in '013579':
#             for a4 in '013579':
#                 for a5 in '013579':
#                     for a6 in '013579':
#                         for a7 in '013579':
#                             for a8 in '013579':
#                                 for a9 in '013579':
#                                     for a10 in '013579':
#                                         total += 1
#
# print(total)
