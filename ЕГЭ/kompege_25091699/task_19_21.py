def f(a, b, count):
    if a + b >= 132:
        return count % 2 == 0
    if count == 0:
        return False
    moves = [f(a + 2, b, count - 1), f(a, b + 2, count - 1),
             f(a * 2, b, count - 1), f(a, b * 2, count - 1),
             f(a * 3, b, count - 1), f(a, b * 3, count - 1)]
    if count % 2 == 0:
        return all(moves)
    return any(moves)


print(19, [s for s in range(1, 100) if f(31, s, 2)])
print(20, [s for s in range(1, 100) if f(31, s, 3) and not f(31, s, 1)])
print(21, [s for s in range(1, 100) if f(31, s, 4) and not f(31, s, 2)])
