P = [i for i in range(2, 21, 2)]
Q = [i for i in range(3, 31, 3)]

for x in range(1, 100):
    f = x in P and x in Q
    if f:
        print(x)
