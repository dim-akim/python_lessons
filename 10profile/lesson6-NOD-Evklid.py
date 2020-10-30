a = 10
b = 4

if b > a:
    a, b = b, a

while b > 0:
    ostatok = a % b
    a, b = b, ostatok

print(a)
