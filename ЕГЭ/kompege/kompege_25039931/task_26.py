# with open('26_12933.txt') as file:
#     n, k = [int(i) for i in file.readline().split()]
#     details_s = []
#     details = []
#     for i in range(1, n + 1):
#         s, o = [int(i) for i in file.readline().split()]
#         details.append((s, i, 'шлиф'))
#         details.append((o, i, 'окрас'))
#
# details.sort()
# conveer = [0] * n
# left = 0
# right = len(conveer) - 1
# ignore = []
# print(details)
#
#
# for item in details:
#     # duration, number, work = item
#     if item[2] == 'шлиф' and item[1] not in ignore:
#         conveer[left] = item[1]
#         ignore.append(item[1])
#         left += 1
#     elif item[2] == 'окрас' and item[1] not in ignore:
#         conveer[right] = item[1]
#         ignore.append(item[1])
#         right -= 1
#
# print(conveer)
# print(f'{left=} {right=} {conveer[k-1]=}')

with open('26_12478.txt') as file:
    n, ege_start, ege_end = [int(i) for i in file.readline().split()]
    watchers = []
    for line in file:
        start, end = line.split()
        watchers.append((int(start), int(end)))

watchers.sort()

total = 0
max_end = 0
cur_start = 0

# for item in watchers:
#     start = item[0]
#     end = item[1]

for start, end in watchers:
    if start <= ege_start and end > max_end:
        cur_start = start
        max_end = end

    elif start > ege_start:
        total += 1
        print(f'{total} {cur_start=} {max_end=}')
        ege_start = max_end

    elif end > ege_end:
        total += 1
        print(f'{total} {start=} {end=}')
        break



