import time


def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield  # отдает управление потоком. В этот момент можно вызвать другой генератор


def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield  # отдает управление потоком. В этот момент можно вызвать другой генератор


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        time.sleep(.5)


if __name__ == '__main__':
    queue = []  # имитируем очередь. Будем брать первый элемент с помощью pop(0)
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
