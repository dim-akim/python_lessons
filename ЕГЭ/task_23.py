# """
# Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
#
# 1.Прибавить 1
# 2.Прибавить 2
# 3.Умножить на 3
#
# Программа для исполнителя— это последовательность команд.
# Сколько существует программ, которые преобразуют исходное число 2 в число 15,
# и при этом траектория вычислений содержит число 10 и не содержит числа 14?
# """
#
# paths_list = [0, 0, 1]
#
#
# def paths(a, b):
#     if len(paths_list) < b:
#         for i in range(len(paths_list), b + 1):
#
#             paths_list.append(paths(a, i-1) + paths(a, i-2) + (paths(a, i // 3) if i % 3 == 0 else 0))
#     if b == 14:
#         paths_list[b] = 0
#     print(paths_list)
#     return paths_list[b]
#     # if a > b:
#     #     return 0
#     # elif a == b:
#     #     return 1
#     # elif a == 14:
#     #     return 0
#     # return paths(a + 1, b) + paths(a + 2, b) + paths(a * 3, b)
#
#
# # print(paths(2, 10) * paths(10, 15))
# print(paths(2, 15))

from functools import lru_cache  # кэширует вычисленные значения
import itertools
import fnmatch
import ipaddress


@lru_cache()
def find_paths(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    elif a == 25:
        return 0
    return find_paths(a + 3, b) + find_paths(a * 2, b) + find_paths(a * 5, b)


def find_paths_from_5(b):
    if len(paths) <= b:
        for i in range(len(paths), b + 1):
            result = find_paths_from_5(i - 3)
            if i % 2 == 0:
                result += find_paths_from_5(i // 2)
            if i % 5 == 0:
                result += find_paths_from_5(i // 5)
            paths.append(result)
            if i == 25:
                paths[i] = 0
    return paths[b]


paths = [0, 0, 0, 0, 0, 1]

# print(find_paths(5, 115))
print(find_paths_from_5(115))
