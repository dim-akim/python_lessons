number = int(input())

eurasia_war_flag = True

while number != 0:
    question = input()

    if question == 'С кем война?':
        if eurasia_war_flag:
            print('Евразия')
        else:
            print('Остазия')
    elif question == 'С кем мир?':
        if eurasia_war_flag:
            print('Остазия')
        else:
            print('Евразия')
    if question == 'Меняем':
        eurasia_war_flag = not eurasia_war_flag

    number -= 1

