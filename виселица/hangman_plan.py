def main():
    """
    Главная функция. Отрисовывает экран
    и вызывает функцию обработки пользовательского ввода
    :return:
    """
    words = get_words()
    word = choose_word(words)
    while True:
        draw_screen()
        reaction()


def get_words():
    """
    TODO вытащить список слов из таблицы Excel
    :return:
    """
    words = [
        'Мама',
        'Папа',
        'Школа'
    ]
    return words


def choose_word(list_of_words):
    return list_of_words[0]


def draw_screen():
    draw_right_half()
    draw_left_half()


def reaction():
    # if letter == 'Н':
    pass


def draw_right_half():
    pass


def draw_left_half():
    pass


main()
