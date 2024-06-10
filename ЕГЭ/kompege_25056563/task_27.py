
with open('27B_4685.txt') as file:
    n, m = [int(i) for i in file.readline().split()]
    bistros = [int(line) // 6 + bool(int(line) % 6) for line in file]

print(bistros)
track = [0] * n
for i in range(m, len(bistros) - m):
    ratios = sum(bistros[i-m:i+m+1])
    track[i] = ratios

print(track)
