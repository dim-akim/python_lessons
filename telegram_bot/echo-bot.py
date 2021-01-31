from telegram import Bot, Update
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
from telegram_bot.settings import TOKEN, ADMIN_IDS


def main():
    # класс, который ловит обновления из телеграма и передает их диспетчеру
    # по сути, фронтенд для бота. Лучше создавать, используя параметр token, а не параметр bot
    updater = Updater(
        token=TOKEN,
        use_context=True  # Для обратной совместимости с версиями 12 и ниже
    )

    # Обработчик команды
    secret_command_handler = CommandHandler('secret', secret_command)

    # Обработчик обычного сообщения с фильтром
    message_handler = MessageHandler(Filters.text, do_echo)

    # Диспетчер распределяет события по обработчикам
    dispatcher = updater.dispatcher

    # Добавляем обработчики. Порядок важен - если какой-то обработчик поймает событие, то дальше оно не пойдет!
    dispatcher.add_handler(secret_command_handler)

    dispatcher.add_handler(message_handler)

    # Начинаем бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context):
    """
    Отправляет в чат эхо: id написавшего и текст сообщения
    :param update:
    :param context:
    :return:
    """
    chat_id = update.message.chat_id
    text = update.message.text

    reply_text = f'Ваш {chat_id=}\n\n{text=}'
    update.message.reply_text(  # аналог context.bot.send_message
        text=reply_text
    )


def admin_access(f):
    """
    Декоратор, который ограничивает доступ к команде только для chat_id, которые перечислены в ADMIN_IDS
    :param f:
    :return:
    """
    def wrapper(*args, **kwargs):
        update = args[0]

        if update and hasattr(update, 'message'):
            chat_id = update.message.chat_id
            if chat_id in ADMIN_IDS:
                print(f'Доступ разрешен для {chat_id=}')
                return f(*args, **kwargs)
            else:
                print(f'Доступ запрещен для {chat_id=}')
        else:
            print('Нет атрибута update.message')

    return wrapper


@admin_access
def secret_command(update: Update, context):
    reply_text = f'Секретик!'
    update.message.reply_text(
        text=reply_text
    )


def answer_with_keyboard(update: Update, context: CallbackContext) -> None:
    # Для клавиатуры нужна матрица (двумерный список) из текстовых элементов
    # Каждый текстовый элемент - отдельная кнопка

    button_list = [
        [
            'ряд1 колонка1',
            'ряд1 колонка2',
            'ряд1 колонка3'
        ],
        [
            'ряд2 колонка1',
            'ряд2 колонка2'
        ]
    ]
    # Можно в качестве кнопок использовать объект KeyboardButton
    # button_list = [
    #     [
    #         KeyboardButton("col1"),
    #         KeyboardButton("col2")
    #     ],
    #     [KeyboardButton("row 2")]
    # ]

    # Теперь собираем кнопки в клавиатуру - объект ReplyKeyboardMarkup
    # Для одной кнопки в строке можно использовать одномерный список и метод from_column
    reply_markup = ReplyKeyboardMarkup(
        button_list,  # список кнопок
        resize_keyboard=True,  # сжимает кнопки по вертикали до высоты текста
        one_time_keyboard=True  # убирает клавиатуру после нажатия на кнопку
    )
    update.message.reply_text("Меню с тремя колонками", reply_markup=reply_markup)


if __name__ == '__main__':
    main()
