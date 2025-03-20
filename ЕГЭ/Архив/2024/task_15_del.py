# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))

for A in range(1, 100):
    for x in range(1, 10000):
        if ((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0))) == 0:
            break
    else:
        print(A)
    # if x == 9999:
    #     print(A)
