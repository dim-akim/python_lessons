"""
Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:

1.Прибавить 1
2.Прибавить 2
3.Умножить на 3

Программа для исполнителя— это последовательность команд.
Сколько существует программ, которые преобразуют исходное число 2 в число 15,
и при этом траектория вычислений содержит число 10 и не содержит числа 14?
"""

paths_list = [0, 0, 1]


def paths(a, b):
    if len(paths_list) < b:
        for i in range(len(paths_list), b + 1):

            paths_list.append(paths(a, i-1) + paths(a, i-2) + (paths(a, i // 3) if i % 3 == 0 else 0))
    if b == 14:
        paths_list[b] = 0
    print(paths_list)
    return paths_list[b]
    # if a > b:
    #     return 0
    # elif a == b:
    #     return 1
    # elif a == 14:
    #     return 0
    # return paths(a + 1, b) + paths(a + 2, b) + paths(a * 3, b)


# print(paths(2, 10) * paths(10, 15))
print(paths(2, 15))
