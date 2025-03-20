def func(n: str):
    while '12' in n or '322' in n or '222' in n:
        if '12' in n:
            n = n.replace('12', '2', 1)
        if '322' in n:
            n = n.replace('322', '21', 1)
        if '222' in n:
            n = n.replace('222', '3', 1)
    return n


for n in range(3, 10000):
    s = '1' + '2' * n
    s = func(s)
    if sum(int(i) for i in s) == 15:
        print(n)
