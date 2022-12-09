# Дважды почти одинаковый код, как можно улучшить?

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
d = 0
t = 0
if a > b:
    for num in range(b,a+1):
        if num % 3 == 0:
            d += num
            t += 1
        else:
            continue
else:
    for num in range(a,b + 1):
        if num % 3 == 0:
            d += num
            t += 1
        else:
            continue
d /= t
print('Среднее значение всех чисел, которые делятся на 3:', d)