# def f(a, b, cnt=0):
#
#     if a == b:
#         return 1
#     if a - 2 > b:
#         return 0
#
#     return (f(a - 1, b, cnt+1) if cnt < 2 else 0) + f(a + 5, b) + f(a * 2, b)
#
#
# print(f(5, 34))

def f(a, b, cnt_a=0, cnt_b=0):
    if a < b:
        return 0
    if a == b:
        return 1
    res1 = (f(a - 2, b, cnt_a + 1)) if cnt_a < 2 else 0
    if cnt_b >= 2:
        res2 = 0
    else:
        if a % 2 == 0:
            res2 = f(a // 2, b, 0, cnt_b + 1)
        else:
            res2 = f(a - 7, b, 0, cnt_b + 1)
    return res1 + res2

print(f(40, 1))
