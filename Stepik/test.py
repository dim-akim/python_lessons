a = []
n = 6
for i in range(0, n):
    a.append(int(input()))

j = min(k for k in a if k % 6 != 0)
for k in range(n):
    if a[k] % 6 != 0:
        a[k] = j
    print(a[k])
