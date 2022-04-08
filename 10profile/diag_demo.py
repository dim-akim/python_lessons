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


def task5():
    #
    for i in range(1, 300):
        s = i
        n = 200
        while s > 0:
            s = s // 4
            n = n - 6
        print(i, n)
        if n == 170:
            break


def task11():
    # T - trajectories (тракетории)
    T = [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    for i in range(13, 73):
        T.append(T[i - 1])  # добавляем i-ый элемент
        if i >= 36 and i % 3 == 0:
            print(T[i // 3])
            T[i] += T[i // 3]  # T[i] = T[i] + T[i // 3]
        if i == 24:
            T[i] = 0
        print(T)


def task12():
    #
    for i in range(1, 1000):
        x = i
        L = 0
        M = 0
        while x > 0:
            L = L + 1
            if M < (x % 8):
                M = x % 8
            x = x // 8
        print(i, L, M)
        if L == 4 and M == 7:
            break


task11()
