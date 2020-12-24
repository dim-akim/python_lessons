from openpyxl import load_workbook as lw


def main():
    # открыть базу данных
    print('Начало работы')

    while True:
        answer = listen()

        if answer == 'start':
            pass
        elif answer == 'help':
            print(show_help())
        elif answer == 'reg_task':
            pass
        else:
            print('Неправильная команда.')


def listen():
    print('Введите команду (start, help, reg): ')
    return input()


def show_help():
    return ''' start - команда, которая запускает весь процесс
    help - команда, которая выводит описание всех остальных команд
    reg_task - запускает процесс заполнения заявки
    show_tasks - показывает все имеющиеся заявки
    статус заявки - показывает статус заявки 
    '''


def reg_task():
    pass


main()
