a = [i for i in input().lower().split()]
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(i, d[i])
