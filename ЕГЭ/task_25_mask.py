# 20@@22#
# 10980

def is_even(s):
    for i in s:
        if int(i) % 2 > 0:
            return False
    return True

for i in range(10980, 10**10, 10980):
    number = str(i)
    if (
            number[:2] == '20' and
            number[4:6] == '22' and
            number[2] in '13579' and
            number[3] in '13579' and
            is_even(number[6:])
    ):
        print(i, i // 10980)
