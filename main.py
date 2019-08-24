from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Updater

from config import REQUEST_KWARGS, TOKEN



#Подключаем token и proxy
updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)



#Функции  callback
def do_start(bot:Bot, update:Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Привет, отправь мне первое сообщение.'
    )


def do_help(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Я только тренировочный бот, ничем не могу помочь. 😔'
    )









#Обработчики событий
start_handler = CommandHandler('start', do_start)
help_handler = CommandHandler('help', do_help)


#Регистрация обработчика
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)


updater.start_polling()