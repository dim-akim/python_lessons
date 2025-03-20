print('z y x w')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                impr = (x or not y) and (not (x == z)) and w
                if impr == 1:
                    print(z, y, x, w)
