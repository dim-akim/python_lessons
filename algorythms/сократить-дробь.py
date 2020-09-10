b = int(input())
a = int(input())

d = a
c = b
while b != 0:
    t = a % b
    a = b
    b = t

print(c // a)
print(d // a)
