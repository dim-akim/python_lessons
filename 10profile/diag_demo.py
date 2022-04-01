def task1():
    s = '7' * 2022
    while '777' in s or '333' in s:
        s = s.replace('777', '3', 1)
        s = s.replace('333', '7', 1)
    print(s)


def task2():
    # разобраться с алгеброй логики
    pass


def task3():
    # уже разбирали. НА ДОМ!
    pass


def task4():
    for n in range(1, 10):
        r = bin(n)  # строим двоичное число вида 0bxxxx
        r = r[2:]  # берем двоичное число без первых двух символов, т.е. остается только хххх
        if n % 2 == 0:  # if r[-1] == '0'
            r += '10'
        else:
            r += '11'
        if r.count('1') % 2 == 0:
            r += '0'
        else:
            r += '1'
        if int(r, 2) > 53:
            print(n)
            break
        print(r, int(r, 2))


task4()
