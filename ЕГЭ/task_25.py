# # Маска 2?1*67 делятся на 159
# a = '2'
# c = '1'
# e = '67'
# numbers = []
# for b in '0123456789':
#     number = int(a + b + c + e)
#     if number % 159 == 0:
#         numbers.append((number, number // 159))
#     for d in range(100):
#         number = int(a + b + c + str(d) + e)
#         if number % 159 == 0:
#             numbers.append((number, number // 159))
#
# for item in sorted(numbers):
#     print(*item)

for number in range(159, 10**7 + 1, 159):
    n = str(number)
    if n[0] == '2' and n[2] == '1' and n[-2:] == '67':
        print(number, number // 159)
