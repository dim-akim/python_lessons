def paths(a, b):
    if a == b:
        return 1
    elif a > b:
        return 0
    # прописываем, какую позицию надо избегать
    result = paths(a + 1, b) + paths(a * 2, b)
    if a % 3:
        result += paths(a + a % 3, b)
    return result


print(paths(3, 11) * paths(11, 18))
