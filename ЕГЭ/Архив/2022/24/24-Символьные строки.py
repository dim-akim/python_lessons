"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.

Для выполнения этого задания следует написать программу.
Ниже приведён файл, который необходимо обработать с помощью данного алгоритма (24_demo.txt)
"""

current_length = max_length = 1

with open('24_demo.txt') as file:
    for line in file:
        for i in range(1, len(line)):
            if line[i] != line[i-1]:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                current_length = 1

print(max_length)
