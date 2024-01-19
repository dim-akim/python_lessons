print('x y z w')  # TODO дорешать

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) or (z <= w)) and (not (x <= w))
                if not f:
                    if x == 1 and y == 1 and w == 0:
                        print(x, y, z, w, f)
                # else:
                #     if (x, y, z, w).count(1) >= 2 or (x, y, z, w).count(0) >= 1 and (x, y, z, w).count(1) >= 1:
                #         print(x, y, z, w, f)
