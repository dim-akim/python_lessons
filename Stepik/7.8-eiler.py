"""
a^5 + b^5 + c^5 + d^5 == e^5
"""

N = 151

for e in range(10, N):
    print(e)
    for a in range(1, e-3):
        for b in range(a+1, e-2):
            for c in range(b + 1, e-1):
                for d in range(c + 1, e):
                    sum5 = a ** 5 + b ** 5 + c ** 5 + d ** 5
                    e5 = e ** 5
                    if sum5 == e5:
                        print("Найдены числа:", a, b, c, d, e)
                        print("Сумма чисел:", a + b + c + d + e)
                    elif sum5 > e5:
                        break
