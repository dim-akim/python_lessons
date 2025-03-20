numbers = []

with open('Demo_files/Доп.файлы/Задание 17/17.txt') as file:
    for line in file:
        numbers.append(int(line))

max_3 = -10001
for number in numbers:
    if number % 10 == 3:
        max_3 = max(max_3, number)

count = 0
max_sum = 0
for i in range(len(numbers) - 1):
    a, b = abs(numbers[i]), abs(numbers[i+1])
    if a % 10 == 3 and b % 10 != 3 or a % 10 != 3 and b % 10 == 3:
        if a ** 2 + b ** 2 >= max_3 ** 2:
            count += 1
            max_sum = max(max_sum, a ** 2 + b ** 2)

print(f'{count=} {max_sum=}')
