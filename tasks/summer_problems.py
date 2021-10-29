def find_path(num):
    global wrong_plants
    global connections
    if visited[num]:
        wrong_plants += connections
        connections = []
        # for i in range(len(visited)):
        #     if not visited[i]:
        #         find_path(i)
        return
    visited[num] = 1
    connections.append(num + 1)
    find_path(plants[num] - 1)


wrong_plants = []
connections = []
with open('summer_problems.txt') as file:
    n = int(file.readline())
    plants = [0] * n
    visited = [0] * n
    for i in range(n):
        plant = int(file.readline())
        plants[i] = plant

print(plants)
print(find_path(0))
print(len(wrong_plants), wrong_plants)
print(connections)
s = 0
for i in visited:
    if not i:
        s += 1
print(s)

