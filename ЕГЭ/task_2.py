print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x or y) <= (z == x)
            if not F:
                print(x, y, z, F)
