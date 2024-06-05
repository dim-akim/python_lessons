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
# max_chain = 0
# with open('24_test.txt') as file:
#     for line in file:
#         chains = []
#         cur_chain = line[0]
#         for i in range(1, len(line.strip())):
#             if line[i - 1] == line[i]:
#                 cur_chain += line[i]
#             else:
#                 chains.append(cur_chain)
#                 cur_chain = line[i]
#         char = sorted(chains, key=len)[-1][0]
#         count = line.count(char)
#         max_chain = max(max_chain, count)
#         print(f'{line=} {chains=} {char=} {count=} {max_chain=}')

# with open('24 (1).txt') as file:
#     lines = file.readline().strip().replace('E', 'E E').split(' ')
#
# count = 0
# for line in lines:
#     if len(line) >= 12 and 'F' not in line:
#         count += 1
#
# print(count)

# max_length = 0
# with open('inf_26_04_21_24.txt') as file:
#     for line in file:
#         line = line.strip()
#         if line.count('G') < 25:
#             for letter in line:
#                 length = line.rfind(letter) - line.find(letter)
#                 max_length = max(max_length, length)
#
# print(max_length)
#
# with open('24 (2).txt') as file:
#     lines = file.readline().split('E')
# print(lines)
# letters = {letter: 0 for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM'}
#
# for line in lines:
#     if line:
#         letter = line[0]
#         letters[letter] += 1
#
# answer = ('', 0)
# for i in letters:
#     if letters[i] > answer[1]:
#         answer = (i, letters[i])
#
# print(answer)

with open('24 (3).txt') as file:
    letters = file.readline()

indexes = [i for i in range(len(letters) - 1) if letters[i] + letters[i+1] == 'WW']

max_len = 0
for i in range(len(indexes) - 102):
    max_len = max(max_len, indexes[i + 102] - indexes[i])

print(indexes)
print(max_len)
# 0 1  2  3   4   5   6
# 3 5 12 82 140 151 152
