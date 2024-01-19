with open('17_10719.txt') as file:
    numbers = [int(line) for line in file]

max_sum = -10_000
total = 0

for i in range(len(numbers) - 3):
    a, b = numbers[i], numbers[i + 3]
    _a, _b = abs(a), abs(b)

    if _a % 100 == 13 and _b % 100 != 13 or _a % 100 != 13 and _b % 100 == 13:
        total += 1
        max_sum = max(max_sum, a + b)
        print(f'{total=} {i}:{a=} {i+3}:{b=} {max_sum=}')

print(f'{total=} {max_sum=}')
