from functools import lru_cache
import sys

# sys.setrecursionlimit(3000)

@lru_cache()
def f(n):
    if n >= 2025:
        return 1
    return n - f(n + 2) - f(n + 4)


for i in range(2025, 19, -1):
    f(i)

print(f(20) + f(25))
