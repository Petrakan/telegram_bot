from telegram import Bot, Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

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

def do_echo(bot, update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )


#Обработчики событий
start_handler = CommandHandler('start', do_start)
help_handler = CommandHandler('help', do_help)
message_handler = MessageHandler(Filters.all, do_echo)


#Регистрация обработчика
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()