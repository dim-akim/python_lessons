# # numbers = []
# count = 0
# max_pare = -20001
#
# with open('17_test.txt') as file:
#     numbers = [int(number) for number in file]
#     # for number in file:
#     #     numbers.append(int(number))
#
# for i in range(len(numbers) - 1):
#     if numbers[i] % 3 == 0 or numbers[i+1] % 3 == 0:
#         count += 1
#         if numbers[i] + numbers[i+1] > max_pare:
#             max_pare = numbers[i] + numbers[i+1]
#         # max_pare = max(max_pare, numbers[i] + numbers[i+1])
#
# print(count, max_pare)

# with open('17 (1).txt') as file:
#     numbers = [int(number) for number in file]
#
# numbers_even = sorted(i for i in numbers if i % 2 == 0)
# numbers_odd = sorted(i for i in numbers if i % 2 == 1)
# print(len(numbers_even), len(numbers_odd))
#
# count = 0
# found_even = 0
# found_odd = 0
# max_even = 0
# max_odd = 0
# for i in range(len(numbers_even)):
#     if numbers_even[i] % 31 == 0:
#         count += len(numbers_even) - 1 - found_even
#         found_even += 1
#         max_even = max(max_even, numbers_even[i])
#
# for i in range(len(numbers_odd)):
#     if numbers_odd[i] % 31 == 0:
#         count += len(numbers_odd) - 1 - found_odd
#         found_odd += 1
#         max_odd = max(max_odd, numbers_odd[i])
#
# max_sum = max(max_even + numbers_even[-1], max_odd + numbers_odd[-1])

# for i in range(len(numbers) - 1):
#     for j in range(i+1, len(numbers)):
#         if (numbers[i] - numbers[j]) % 2 == 0 and (numbers[i] % 31 == 0 or numbers[j] % 31 == 0):
#             count += 1
#             max_sum = max(max_sum, numbers[i] + numbers[j])

# print(count, max_sum)

# with open('17 (3).txt') as file:
#     numbers = [int(line) for line in file]
#
# count_pairs = 0
# max_sum = 0
#
# for i in range(len(numbers)-1):
#     for j in range(i+1, len(numbers)):
#         a, b = numbers[i], numbers[j]
#         if a * b % 26 == 0:
#             count_pairs += 1
#             max_sum = max(a + b, max_sum)
#
# print(f'{count_pairs=} {max_sum=}')

with open('17 (4).txt') as file:
    numbers = [int(line) for line in file]

min6 = min(i for i in numbers if abs(i) % 10 == 6)

count_pairs = 0
max_sum = 0
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    _a, _b = abs(a), abs(b)
    if _a % 10 == 6 and _b % 10 != 6 or _b % 10 == 6 and _a % 10 != 6:
        if a * a + b * b < min6 * min6:
            count_pairs += 1
            max_sum = max(max_sum, a * a + b * b)

print(f'{count_pairs=} {max_sum=}')
