from itertools import permutations


number = set(permutations('нннчччччччч'))
count = 0
for i in number:
    i = ''.join(i)
    if 'нн' not in i:
        if i[0] == 'ч':
            count += 3 * 4**10
        else:
            count += 4 * 4**10

print(count)