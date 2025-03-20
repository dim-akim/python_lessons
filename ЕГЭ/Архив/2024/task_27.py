# 38604
with open('27_B.txt') as file:
    n = file.readline()
    min_sums = [0 for i in range(43)]
    min_lens = [0] + [int(n) for i in range(42)]
    max_sum = 0
    min_len = n
    cur_len = 0
    cur_sum = 0

    for line in file:
        number = int(line)
        cur_sum += number
        cur_len += 1
        d = cur_sum % 43
        if min_sums[d] == 0:
            min_sums[d] = cur_sum
            min_lens[d] = cur_len
        if cur_sum - min_sums[d] > max_sum:
            max_sum = cur_sum - min_sums[d]
            min_len = cur_len - min_lens[d]

print(min_sums)
print(min_lens)

print(min_len)