from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 20:
        return n
    return (n - 6) * f(n - 7)


answers = [n for n in range(20)]

def f2(n):
    if n >= len(answers):
        for i in range(len(answers), n + 1):
            answers.append((i - 6) * f2(i - 7))
    return answers[n]


for i in range(1, 50000):
    f(i)

print((f(47872) - 290 * f(47865)) / f(47858))
