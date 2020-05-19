a = int(input())
b = int(input())
m = int(input())
n = int(input())

print(end='\t')
for j in range(m, n + 1):
    print(j, end='\t')
print()

for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(m, n + 1):
        print(i * j, end='\t')
    print()

