with open('17.txt') as file:
    numbers = [int(line) for line in file]

min7 = min(i for i in numbers if abs(i) % 7 == 0 and abs(i) % 10 == 7)

ans = []
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i+1]
    _a, _b = abs(a), abs(b)
    if (99 < _a < 1000 or 99 < _b < 1000) and a + b > min7:
        ans.append(a**2 + b**2)

print(len(ans), max(ans))
