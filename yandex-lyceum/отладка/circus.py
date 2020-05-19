target = int(input())
steps = 0

while target != 1:
    if target % 2 == 0:
        target = target // 2
    else:
        target -= 1
    steps += 1

print(steps)
