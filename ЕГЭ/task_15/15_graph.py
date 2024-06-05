# for A in range(1000):
#     flag = True
#     for x in range(1000):
#         for y in range(1000):
#             f = ((x <= 9) <= (x*x <= A)) and ((y*y <= A) <= (y <= 9))
#             if not f:
#                 flag = False
#                 break
#         if not flag:
#             break
#
#     if flag:
#         print(A)
#
# for A_left in range(-100, 100):
#     for A_right in range(A_left, 101):
#         flag = True
#         for x in range(-100, 100):
#             for y in range(-100, 100):
#                 f = ((A_left <= x <= A_right) <= (x*x <= 81)) and ((y * y <= 36) <= (A_left <= y <= A_right))
#                 if not f:
#                     flag = False
#                     break
#             if not flag:
#                 break
#
#         if flag:
#             print(A_right - A_left)

# for A in range(1000):
#     flag = True
#     for x in range(1000):
#         f = (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))
#         if not f:
#             flag = False
#             break
#
#     if flag:
#         print(A)

for A in range(1, 1000):
    flag = True
    for x in range(1000):
        f = (x % A > 0) <= ((x % 6 == 0) <= (x % 4 != 0))
        if not f:
            flag = False
            break

    if flag:
        print(A)

