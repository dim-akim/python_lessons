# number = 9**11 * 3**20 - 3**9 - 27
#
# number_3 = ''
# count_2 = 0
#
# while number:
#     number_3 += str(number % 3)
#     if number % 3 == 2:
#         count_2 += 1
#     number //= 3
#
# print(number_3[::-1])
# print(count_2)

# number = 36**8 + 6**20 - 12
# number_6 = ''
# count = 0
# while number > 0:
#     number_6 += str(number % 6)
#     if number % 6 == 5:
#         count += 1
#     number //= 6
#
# print(number_6[::-1])
# print(count)

# for x in '0123456789ABCDE':
#     number = int(f'123{x}5', 15) + int(f'1{x}233', 15)
#     if number % 14 == 0:
#         print(x, number // 14)

'58x723y49'

for x in range(39):
    for y in range(39):
        num = 5 * 39**8 + 8 * 39**7 + x * 39**6 + 7 * 39**5 + 2 * 39**4 + 3 * 39**3 + y * 39**2 + 4 * 39 + 9
        yx = y * 39 + x
        if num % 38 == 0 and int(yx ** 0.5) == yx ** 0.5:
            print(yx)
