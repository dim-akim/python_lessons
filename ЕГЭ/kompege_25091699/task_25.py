for number in range(10**7, 8904575 - 1, -25):
    s = str(number)
    if '89' == s[:2] and '45' == s[3:5] and '75' == s[-2:]:
        print(number, number // 25)
