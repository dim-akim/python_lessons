f_list = [1, 1, 1, 1]


def f(n):
    if n >= len(f_list):
        for i in range(len(f_list), n+1):
            f_list.append((i + 3) * f(i-2))

    return f_list[n]


for j in range(10):
    print(f'{f(j)=} ')
    print(f_list)
