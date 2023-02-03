def find_paths(n):
    if n == 3:
        return 1
    elif n % 3 > 0:
        return 0
    return find_paths(n // 3) + find_paths(n - 3)


print(find_paths(93))
