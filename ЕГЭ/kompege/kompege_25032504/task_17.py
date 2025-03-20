with open('17_11460.txt') as file:
    numbers = [int(line) for line in file]


def begins_with(number, n):
    return str(abs(number))[0] == str(n)


def begins_with_(number, n):
    number = abs(number)
    while number >= 10:
        number //= 10
    return number == n


max_8 = max(int(i) for i in numbers if begins_with(i, 8))
total = 0
min_sum = 100000
for i in range(len(numbers) - 3):
    a, b, c = numbers[i:i+3]
    count_6 = 0
    for number in a, b, c:
        if begins_with(number, 6):
            count_6 += 1
    if count_6 <= 1 and a + b + c >= max_8:
        total += 1
        min_sum = min(min_sum, a + b + c)

print(total, min_sum)
