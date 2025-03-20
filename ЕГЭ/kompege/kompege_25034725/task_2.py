print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not (x <= (not (z <= w))) and ((not z) <= ((not w) == y))
                if f:
                    print(x, y, z, w)
