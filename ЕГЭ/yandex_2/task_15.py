# not A or B or C = 1

C = [-10, -4, 2, 15, 23]
B = [-42, -10, -8, 2, 16]
notA = []
A = []

for x in range(-100, 100):
    if x not in C and x not in B:
        notA.append(x)
    else:
        A.append(x)

print(notA)
print(A)
