with open('17.txt') as file:
    numbers = [int(line) for line in file]

total = 0
max_ab = 0

for i in range(len(numbers) - 1):
    for j in range(i+1, len(numbers)):
        a, b = numbers[i], numbers[j]
        _a, _b = abs(a), abs(b)
        if _a * _b % 26 == 0:
            total += 1
            max_ab = max(max_ab, a + b)

print(total, max_ab)
