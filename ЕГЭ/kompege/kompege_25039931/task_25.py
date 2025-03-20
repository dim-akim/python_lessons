for n in range(2024, 10**10 + 1, 2024):
    n_str = str(n)
    if n_str[0] == '1' and n_str[2] == '2' and n_str[-1] == '4':
        if n ** 0.5 == int(n ** 0.5):
            print(n, n // 2024)
