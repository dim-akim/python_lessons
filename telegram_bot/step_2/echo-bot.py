from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


TOKEN = '1207559312:AAHr0Go-3LMv2VC8PQ9042g2tV4o3LV577o'


def main():
    # объект, который ловит обновления из Телеграма
    updater = Updater(
        token=TOKEN,
    )
    # Диспетчер будет распределять события по обработчикам
    dispatcher = updater.dispatcher

    # Обработчик обычного сообщения с фильтром
    message_handler = MessageHandler(Filters.all, do_echo)
    sticker_handler = MessageHandler(Filters.sticker, do_sticker_echo)

    # Добавляем обработчики. Порядок важен - если какой-то обработчик поймает событие, то дальше оно не пойдет!
    dispatcher.add_handler(sticker_handler)
    dispatcher.add_handler(message_handler)

    # Начинаем бесконечную обработку входящих сообщений
    updater.start_polling()
    print(updater.bot.getMe())
    updater.idle()


def do_echo(update: Update, context: CallbackContext) -> None:
    """
    Отправляет в чат эхо: Приветствие по имени, id написавшего и текст сообщения
    """
    first_name = update.message.from_user.first_name
    chat_id = update.message.chat_id
    text = update.message.text

    update.message.reply_text(  # аналог context.bot.send_message
        text=f'Привет, {first_name}\n'
             f'Ваш {chat_id=}\n\n'  # БОНУС
             f'{text}'
    )


def do_sticker_echo(update: Update, context: CallbackContext) -> None:
    file_id = update.message.sticker.file_id
    update.message.reply_text(
        text=f'Это стикер!\n'
             f'Его {file_id=}'
    )
    update.message.reply_text(
        text='Я тоже так могу!'
    )
    update.message.reply_sticker(
        sticker=file_id
    )


if __name__ == '__main__':
    main()
