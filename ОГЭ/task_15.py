n = int(input())

min_3 = 30000 + 1
for i in range(n):
    number = int(input())
    if number % 3 == 0 and number % 10 == 2:
        # if number < min_3:
        #     min_3 = number
        min_3 = min(min_3, number)

print(min_3)
