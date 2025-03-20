def f(n):
    if len(result) < n:
        for i in range(len(result), n + 1):
            result.append(i * f(i - 1))
    return result[n]

result = [1, 1]
print(f(2023) / f(2020))
