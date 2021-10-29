def primes():
    n = 2
    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0 and n != i:
                break
        else:
            yield n
        n += 1


p = primes()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(range(1, int(4 ** 0.5) + 1))

