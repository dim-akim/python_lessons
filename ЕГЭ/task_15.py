#
# for A in range(1, 1000):
#     like = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             f = (x < A) or (y < A) or (x + 2*y > 50)
#             if not f:
#                 like = False
#                 break
#
#         if not like:
#             break
#
#     if like:
#         print(f'{A=}')
# def treug(n, m, k):
#     return max(n, m, k) < n + m + k - max(n, m, k)
#
#
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         f = not ((treug(x, 11, 18) == (not (max(x, 5) > 68))) and treug(x, A, 5))
#         if not f:
#             flag = False
#             break
#
#     if flag:
#         print(A)

b = range(30, 42)
c = range(50, 57)

answer = []
for a_left in range(1, 100):
    for a_right in range(a_left + 1, 101):
        a = range(a_left, a_right + 1)
        flag = True
        for x in range(1, 1000):
            f = not(((x in b) or (x in c)) <= (x in a))
            if f:
                flag = False
                break
        if flag:
            if len(a) == 27:
                print(a)
            answer.append(len(a))

print(sorted(answer))
