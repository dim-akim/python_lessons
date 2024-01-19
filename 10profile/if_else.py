n = int(input())

if n < 0:
    print('A')
elif n < 5:  # ghost (условие-призрак) n >= 0
    print('B')
elif n < 10:  # ghost n >= 5
    print('C')
else:  # ghost n >= 10
    print('D')
