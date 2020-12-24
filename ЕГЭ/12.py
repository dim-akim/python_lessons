A = [0, 18, 13, 10, 15, 8, 9, 7, 3, 6, 19]

n = 10
s = 0
for i in range(2, n+1):
    if A[i-1] < A[i]:
        t = A[i-1]
        A[i-1] = A[i]
        A[i] = t + 1
        s = s + 1
    print(s, A)

print(3 * s)
