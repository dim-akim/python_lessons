# with open('24_demo.txt') as file:
#     line = file.readline()
#
# count = 1
# max_count = 0
# for i in range(len(line) - 1):  # range(1, len(line)): if line[i] == line[i-1]
#     if line[i] != line[i + 1]:
#         count += 1
#     else:
#         max_count = max(count, max_count)
#         count = 1
#
# print(max_count)

with open('24_prob.txt') as file:
    line = file.readline()

variants = [
    'BAB',
    'BAC',
    'CAB',
    'CAC',
]

max_count = count = flag = 0
for i in range(len(line)):
    if flag > 0:
        flag -= 1
        continue
    elif line[i:i+3] in variants:
        count += 3
        flag = 2
    else:
        max_count = max(count, max_count)
        count = 0

print(max_count)
