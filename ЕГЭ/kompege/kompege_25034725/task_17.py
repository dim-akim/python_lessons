with open('17_11887.txt') as file:
    numbers = [int(line) for line in file]

max_68 = max(i for i in numbers if abs(i) % 100 == 68)

# max_68 = 0
# for i in numbers:
#     if abs(i) % 100 == 68:
#         max_68 = max(i, max_68)

print(max_68)
total = 0
max_sum = 0
for i in range(len(numbers) - 4):
    a, b, c, d = numbers[i:i+4]
    count_2digits = 0
    for j in a, b, c, d:
        if 10 <= j < 100:
            count_2digits += 1
    if count_2digits == 1 or count_2digits == 4:
        if a + b + c + d >= max_68:
            total += 1
            max_sum = max(max_sum, a + b + c + d)

print(total, max_sum)
