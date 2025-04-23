def redaktor(s):
    while '78' in s or '98' in s or '999' in s:
        if '78' in s:
            s = s.replace('78', '8', 1)
        if '98' in s:
            s = s.replace('98', '7', 1)
        if '999' in s:
            s = s.replace('999', '9', 1)
    return s


ans = []
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            s = '7' * i + '8' * j + '9' * k
            result = redaktor(s)
            if sum([int(i) for i in result]) == 801:
                ans.append(len(s))

print(min(ans))
