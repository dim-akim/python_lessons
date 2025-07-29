discret = 96000
time = 213
archive = 0.6
size = 25 * 1024 * 1024 * 8

for n in range(1, 257):
    if 2 * discret * time * n * archive <= size:
        print(n)
