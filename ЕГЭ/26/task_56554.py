# with open('26.txt') as file:
#     n = int(file.readline())
#     coords = [[int(i) for i in line.split()] for line in file]
# print(sorted(coords))

screen = [[0] * 100000] * 100000
with open('26.txt') as file:
    n = int(file.readline())
    for line in file:
        y, x = [int(i)-1 for i in line.split()]
        screen[y][x] = 1

# max_lines = 0
# for row in screen:
#     lines = 0
#     cur_line =
#
#     for col in row:



