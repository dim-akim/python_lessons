# 0 1 2 3

with open('28128_B.txt') as file:
    n = file.readline()
    ost = [0] * 4  # 0 и 3 - остаток 0
    for line in file:
        x = int(line)
        if x % 3 == 0:
            if x > ost[3]:
                ost[0] = ost[3]
                ost[3] = x
            elif x > ost[0]:
                ost[0] = x
        ost[x % 3] = max(ost[x % 3], x)

print(max(ost[0] + ost[3], ost[1] + ost[2]))
