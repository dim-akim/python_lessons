number = 9**11 * 3**20 - 3**9 - 27

number_3 = ''
count_2 = 0

while number:
    number_3 += str(number % 3)
    if number % 3 == 2:
        count_2 += 1
    number //= 3

print(number_3[::-1])
print(count_2)
