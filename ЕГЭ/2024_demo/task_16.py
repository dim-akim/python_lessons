def f(n):
    if n > len(fact):
        for i in range(len(fact), n + 1):
            fact.append(fact[i - 1] * i)
    return fact[n]

fact = [0, 1]

print(f(10) / f(9))
print(fact)
print(f(20))
print(fact)
