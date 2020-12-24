a = []
n = 30
for i in range(0, n):
    a.append(int(input()))
x = 0
y = 0
for i in range(0, n):
    if a[i] == 4 or a[i] == 5:
        x += a[i]
        y += 1
s = x/y
print(s)
