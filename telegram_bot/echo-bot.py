from telegram import Bot, Update
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler
from telegram.utils.request import Request
from telegram_bot.settings import TOKEN, ADMIN_IDS


def main():
    # request = Request(
    #     connect_timeout=1.0,
    #     read_timeout=0.5,
    # )

    # Записываем бота в переменную, чтобы можно было к нему обращаться
    bot = Bot(
        # request=request,
        token=TOKEN,
    )
    print(bot.get_me())

    # TODO что это?
    updater = Updater(
        bot=bot,
        use_context=True
    )

    # Обработчик события
    secret_command_handler = CommandHandler('secret', secret_command)
    updater.dispatcher.add_handler(secret_command_handler)

    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(message_handler)

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


if __name__ == '__main__':
    main()
