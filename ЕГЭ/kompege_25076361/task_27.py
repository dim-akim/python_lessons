def d(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2) ** .5


def center(cluster):
    min_length = 10**10
    ans = None
    for x, y in cluster:
        length = 0
        for x2, y2 in cluster:
            length += d(x, y, x2, y2)
        if length < min_length:
            min_length = length
            ans = (x, y)
    return ans


def knot(*centers):
    min_length = 10**10
    ans = None
    for cluster in clusters:
        for x, y in cluster:
            length = sum([d(x, y, c[0], c[1]) for c in centers])
            if length < min_length:
                min_length = length
                ans = x, y
    return ans


clusters = [[], []]

with open('27_A_19647.txt') as file:
    file.readline()
    for line in file:
        x, y = [float(i) for i in line.replace(',', '.').split()]
        if x > 4:
            clusters[1].append((x, y))
        else:
            clusters[0].append((x, y))


c1, c2 = [center(i) for i in clusters]
trans_knot = knot(c1, c2)

print(trans_knot)
