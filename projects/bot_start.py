from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackContext, ConversationHandler
from datetime import datetime


TOKEN = '1207559312:AAHr0Go-3LMv2VC8PQ9042g2tV4o3LV577o'
HW_DAY, HW_WEEK = range(2)


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', get_homework)
    help_handler = CommandHandler('help', hw_choose_day)
    all_handler = MessageHandler(Filters.all, do_echo)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(all_handler)

    updater.start_polling()
    print('Бот запустился')
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    text = update.message.text
    print(f'Нам написали {text=} {update.message.date=}')
    update.message.reply_text(text=text)


def do_help(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='/reg_task -\t запускает процесс заполнения заявки\n'
             '/status -\t показывает все имеющиеся заявки\n'
             '/my_status_id -\t показывает статус заявки'
    )


def get_homework(update: Update, context: CallbackContext):
    keyboard = ['На сегодня', 'На завтра', 'На неделю']
    update.message.reply_text(
        text='Выберите один из вариантов:',
        reply_markup=ReplyKeyboardMarkup.from_column(keyboard, one_time_keyboard=True)
    )

    return HW_DAY


def hw_choose_day(update: Update, context: CallbackContext):
    today_weekday = datetime.weekday(datetime.today())
    answer = update.message.text

    if answer == 'На сегодня':
        get_homework_today(update, context, today_weekday)
    elif answer == 'На завтра':
        get_homework_tomorrow(update, context, today_weekday)
    elif answer == 'На неделю':
        get_homework_week(update, context)
    else:
        hw_choose_day(update, context)


def get_homework_today(update: Update, context: CallbackContext, weekday_column):
    reply = ''
    print(page.cell(row=1, column=weekday_column).value)

    # for row in homework_rows:
    #     print(page.cell(row=row-1, column=weekday_column).value, end='\t\t')
    #     print(page.cell(row=row, column=weekday_column).value, end='\t\t')
    #     for i in range(1, 3):
    #         if page.cell(row=row, column=weekday_column + i).value is not None:
    #             print(page.cell(row=row, column=weekday_column + i).value, end='\t\t')
    #     print()  # Переход на новую строку.
    update.message.reply_text(text=reply)

    return ConversationHandler.END


if __name__ == '__main__':
    main()
