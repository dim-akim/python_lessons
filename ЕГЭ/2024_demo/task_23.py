def paths(a, n):
    if n == a:
        return 1
    elif n < a:
        return 0
    if n == 11:
        return 0

    result = 0
    if n % 2 == 0:
        result += paths(a, n // 2)
    if int(n ** 0.5) == n ** 0.5:
        result += paths(a, n ** 0.5)
    result += paths(a, n-1)
    return result

print(paths(2, 20))
