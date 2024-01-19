'1?2157*4'

for number in range(2024, 10 ** 10 + 1, 2024):
    num = str(number)
    if num[0] == '1' and num[2:6] == '2157' and num[-1] == '4':
        print(number, number / 2024)
