def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def fib_dynamic(n):
    if n >= len(fib_list):
        for i in range(len(fib_list), n + 1):
            fib_list.append(fib_dynamic(n-1) + fib_dynamic(n-2))
    return fib_list[n]


fib_list = [0, 1]  # Крайний случай рекурсии


print(1, fib(5))
print(2, fib(7))
