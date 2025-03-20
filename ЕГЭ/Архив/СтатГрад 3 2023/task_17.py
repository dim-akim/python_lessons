with open('17.txt') as file:
    numbers = [int(line) for line in file]

min_3 = 10000
for number in numbers:
    if abs(number) % 10 == 3:
        min_3 = min(min_3, number)

max_sum = -1
count = 0
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i+1]
    flag = False
    if abs(a) % 10 == abs(b) % 10:
        if (a % 3 == 0) + (b % 3 == 0) == 1:
            if a ** 2 + b ** 2 <= min_3 ** 2:
                count += 1
                max_sum = max(max_sum, a ** 2 + b ** 2)

print(f'{count=} {max_sum=} {min_3=}')
