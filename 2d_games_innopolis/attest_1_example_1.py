# Несколько таких заданий

number1, number2 = int(input()), int(input()) + 1
my_set = set()
for num in range(number1, number2):
    if num % 3 == 0:
        my_set.add(num)
print(sum(my_set) / len(my_set))