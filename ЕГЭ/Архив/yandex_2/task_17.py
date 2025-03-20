with open('17.txt') as file:
    numbers = [int(line) for line in file]

min_3 = []
for i in numbers:
    if 99 < i < 1000:
        min_3.append(i)

min_3.sort()
min_3 = min_3[1]

total = 0
max_sum = 0
for i in range(len(numbers) - 1):
    if numbers[i] + numbers[i+1] < min_3 ** 2:
        total += 1
        max_sum = max(max_sum, numbers[i] + numbers[i+1])

print(f'{total=} {max_sum=}')
