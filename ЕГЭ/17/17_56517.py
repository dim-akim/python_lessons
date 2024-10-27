with open('17 (1).txt') as file:
    numbers = [int(line) for line in file]

min3 = min(i for i in numbers if abs(i) % 10 == 3)
ans = []

for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    _a, _b = abs(a), abs(b)
    if _a % 10 == _b % 10 and (_a % 3 == 0 and _b % 3 != 0 or _a % 3 != 0 and _b % 3 == 0) and a*a + b*b <= min3**2:
        ans.append(a*a + b*b)

ans.sort()

print(len(ans), ans[-1])
