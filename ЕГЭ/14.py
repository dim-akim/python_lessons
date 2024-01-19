a = 3 * 1024**75 + 2 * 256**76 - 16**77 - 2023

number = []
while a > 0:
    number.append(a % 32)
    a //= 32

number.reverse()
print(len(number), number.count(0), number)
