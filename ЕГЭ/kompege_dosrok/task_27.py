with open('27B_15342.txt') as file:
    n, k = [int(x) for x in file.readline().split()]
    costs = [0] * n
    stations = []
    for line in file:
        km, liters = [int(i) for i in line.split()]
        if liters % 11 == 0:
            trucks = liters // 11
        else:
            trucks = liters // 11 + 1



        stations.append([km, trucks])


for j in range(len(stations)):
    print(j)
    # cost = 0
    # print('Хранилище на километре', base[0])
    # for station in stations:
    #     dist = min(abs(station[0] - base[0]), abs(k - base[0] + station[0]))
    #     cost += dist * station[1]
    #     print(station[0], dist, trucks)
    # costs.append(cost)
    base = stations[j]
    # print('Хранилище на километре', base[0])
    for i in range(len(costs)):
        dist = min(abs(stations[i][0] - base[0]), abs(k - base[0] + stations[i][0]))
        costs[j] += dist * stations[i][1]
        # print(stations[i][0], dist, stations[i][1])

print(min(costs))
