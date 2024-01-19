def f(n):
    if n < 3:
        return result[n]
    if n % 2 == 0:
        return 2 * result[n-2] - result[n-1] + 2
    return 2 * result[n-1] + result[n-2] - 2


def f_2(n):
    if n < 3:
        return 2
    if n % 2 == 0:
        return 2 * f_2(n-2) - f_2(n-1) + 2
    return 2 * f_2(n-1) + f_2(n-2) - 2


result = [2, 2, 2]

for i in range(3, 171):
    result.append(f(i))

print(result[:10])
print(result[170])
print(f_2(170))
