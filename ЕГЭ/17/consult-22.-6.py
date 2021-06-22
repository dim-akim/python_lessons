count = 0
for i in range(4855, 7857):
    if (
            i % 8 == 0 and
            i % 19 == 0 and
            i % 7 != 0 and
            i % 16 != 0 and
            i % 24 != 0 and
            i % 26 != 0
    ):
        count += 1
        print(i)
print(count)
