class Star:
    def __init__(self, coords: str):
        self.x, self.y = [float(i) for i in coords.replace(',', '.').split()]


def d(star1: Star, star2: Star):
    return ((star1.x - star2.x) ** 2 + (star1.y - star2.y) ** 2) ** .5


def center(cluster) -> Star:
    min_length = 10**10
    cent_star = None
    for star1 in cluster:
        sum_length = 0
        for star2 in cluster:
            sum_length += d(star1, star2)
        if sum_length < min_length:
            min_length = sum_length
            cent_star = star1
    return cent_star


cluster_up = []
cluster_down = []
with open('27_A_21911.txt') as file:
    file.readline()
    for line in file:
        star = Star(line)
        if star.y > 2:
            cluster_up.append(star)
        else:
            cluster_down.append(star)

c1 = center(cluster_up)
c2 = center(cluster_down)

px = int((c1.x + c2.x) / 2 * 10000)
py = int((c1.y + c2.y) / 2 * 10000)
print(f'{px=} {py=}')
