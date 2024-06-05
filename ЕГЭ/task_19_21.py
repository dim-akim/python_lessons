def f(a, s, count):
    if s + a >= 464 and count == 0:
        return True
    if count == 0 or s + a >= 464:
        return False

    if count % 2 > 0:
        return f(a + 2, s, count - 1) or f(a, s + 2, count - 1) or f(a * 3, s, count - 1) or f(a, s * 3, count - 1)
    else:
        return f(a + 2, s, count - 1) and f(a, s + 2, count - 1) and f(a * 3, s, count - 1) and f(a, s * 3, count - 1)


print(19, [S for S in range(1, 451) if f(13, S, 2)])
print(20, [S for S in range(1, 451) if f(13, S, 3)])
print(21, [S for S in range(1, 451) if f(13, S, 4)])
# for S in range(1, 451):
#     if f(13, S, 4):
#         print(S)
