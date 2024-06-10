# # for i in range(1000):
# #     n = i
# #     n = bin(n)[2:]
# #     if n.count('1') % 2 == 0:
# #         n += '0'
# #         r = '1' + n[2:]
# #     else:
# #         n += '1'
# #         r = '11' + n[2:]
# #     r = int(r, base=2)
# #
# #     if 30 >= r >= 26:
# #         print(f'{i=} {r=}')
#
# # for i in range(123_456_789, 1_987_654_321):
# # count = 0
# # for i in range(15432098, 248456800):
# #     n = i
# #     r = [int(j) for j in str(n)]
# #     for j in range(3):
# #         if sum(r) % 2 == 0:
# #             n *= 2
# #             r = [int(j) for j in str(n)]
# #         else:
# #             n = 2 * n + 1
# #             r = [int(j) for j in str(n)]
# #     if 123_456_789 <= n <= 1_987_654_321:
# #         count += 1
# #
# # print(count)
#
# # for n in range(1, 1000):
# #     n2 = bin(n)[2:]
# #     if n2.count('1') % 2 == 0:
# #         n2 += '00'
# #     else:
# #         n2 += '10'
# #     r = int(n2, 2)
# #     if r > 97:
# #         print(f'{n=} {r=}')
# #
# # for n in range(1, 1000):
# #     n2 = bin(n)[2:]
# #     n2 += str(n2.count('1') % 2)
# #     n2 += str(n2.count('1') % 2)
# #     r = int(n2, 2)
# #     if r > 97:
# #         print(f'{n=} {r=}')
#
# def to_base(n, base):
#     result = []
#     while n:
#         result.append(str(n % base))
#         n //= base
#     return result[::-1]
#
#
# for n in range(1, 1000):
#     n3 = to_base(n, 16)
#     print(f'{n=} {n3}')
#     # if n % 3 == 0:
#     #     n3 += n3[-3:]
#     # else:
#     #     n3 += to_base(n % 3 * 3, 3)
#     # r = int(n3, 16)
#     # if r > 150:
#     #     print(f'{n=} {n3=} {r=}')
#
# max_len = 0
# current = []
#
# for n in range(1, 10000):
#     n2 = bin(n)[2:]
#     n2 += bin(n % 4)[2:]
#     r = int(n2, 2)
#     current.append(r)
#
# # current.sort()
#
# print(current)

for n in range(1, 100000):
    n2 = bin(n)[2:]
    r = n2[::2].count('0') - n2[1::2].count('1')
    r = abs(r)
    if r == 5:
        print(f'{n=} {r=}')
