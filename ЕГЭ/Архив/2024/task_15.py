# for A in range(1000):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             f = (2*x + 3*y < 30) or (x + y >= A)
#             if not f:
#                 flag = False
#                 break
#         if not flag:
#             break
#
#     if flag:
#         print(A)
#
#
# for A_left in range(-100, 0):
#     for A_right in range(101):
#         flag = True
#         for x in range(-100, 101):
#             f = ((A_left <= x <= A_right) <= (x*x < 100)) and ((x*x <= 64) <= (A_left <= x <= A_right))
#             if not f:
#                 flag = False
#                 break
#
#         if flag:
#             print(A_right - A_left)

# for A in range(100):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             f = (y + 2*x < A) or (x > 30) or (y > 20)
#             if not f:
#                 flag = False
#                 break
#         if not flag:
#             break
#
#     if flag:
#         print(A)
#
# for A in range(1, 1000):
#     flag = True
#     for x in range(1000):
#         f = (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))
#         if not f:
#             flag = False
#             break
#
#     if flag:
#         print(A)
#
# P = [i for i in range(4, 16)]
# Q = [i for i in range(12, 21)]
# min_A = 10000
#
#
# for A_left in range(0, 100):
#     for A_right in range(A_left+1, 100):
#         A = [i for i in range(A_left, A_right + 1)]
#         flag = True
#         for x in range(0, 100):
#             f = ((x in P) and (x in Q)) <= (x in A)  # A_left <= x <= A_right
#             if not f:
#                 flag = False
#                 break
#
#         if flag:
#             min_A = min(min_A, len(A))
# print(min_A)

P = [i for i in range(25, 51)]
Q = [i for i in range(32, 48)]
max_len = 0

for A_left in range(0, 100):
    for A_right in range(A_left, 101):
        flag = True
        for x in range(1000):
            f = ((not (A_left <= x <= A_right)) <= (x in P)) <= ((A_left <= x <= A_right) <= (x in Q))
            if not f:
                flag = False
                break

        if flag:
            max_len = max(A_right - A_left, max_len)

print(max_len)
