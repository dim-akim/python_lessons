total1 = int(input())
total2 = int(input())

while total1 > 0 or total2 > 0:
    number = int(input())
    summ = int(input())
    if number == 1:
        total1 -= summ
    else:
        total2 -= summ
    print(total1, total2)
