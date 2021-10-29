a = 8 ** 2020 + 4 ** 2017 + 26 - 1
count = 0

while a:
    if a % 2 == 1:
        count += 1
    a //= 2

print(count)
