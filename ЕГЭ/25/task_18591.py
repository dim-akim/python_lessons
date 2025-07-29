# Ч9?23?*23НЧ

for number in range(1984, 10**10, 1984):
    s = str(number)
    if (
        int(s[0]) % 2 == int(s[-1]) % 2 == 0 and len(s) >= 10 and
        s[1] == '9' and s[3:5] == s[-4:-2] == '23' and
        int(s[-2]) % 2 != 0
    ):
        print(number, number // 1984)
