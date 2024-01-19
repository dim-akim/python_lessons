"""
А. Прибавить последнюю цифру
В. Добавить остаток от деления на 68
С. Возвести в квадрат
"""

path2_list = [0, 0, 1] + [0] * 66
path68_list = [1]


def paths(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif a == 100:
        return 0
    result = 0
    if a % 10 != 0:
        result += paths(a + a % 10, b)  # A
    result += paths(a + a % 68, b)  # B
    result += paths(a ** 2, b)  # C

    return result


def paths2(n):
    if n > len(path2_list):
        for i in range(len(path2_list), n + 1):
            last_dig = i % 10
            if last_dig > 0:
                path2_list[i + last_dig] += path2_list[i]
            ost_68 = i % 68
            path2_list[i + ost_68] += path2_list[i]
            path2_list[i + i ** 2] += path2_list[i]


print(paths(2, 68) * paths(68, 680))
