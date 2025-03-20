def f(a, b):
    if a == b == 0:
        return 0
    elif a > b:
        return f(a-1, b) + b
    elif a <= b and b > 0:
        return f(a, b-1) + a


x = 1048576
count = 0
for i in range(1, int(1048576**0.5) + 1):
    if x % i == 0:
        count += 2
        print(f'{count=} {i=} {x//i = }')
