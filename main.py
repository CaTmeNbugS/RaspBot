from DateHandler   import DateHandler, isDateHandler
from QueryHandler  import QueryHandler, isQueryHandler
from MessageHandler import MessageHandler, isMessageHandler

from command import command

import logging
import telebot

bot = telebot.TeleBot(API_TOKEN)

logging.basicConfig(
    level = logging.INFO,
    filename = "audit.log", 
    format = "%(asctime)s - %(message)s", 
)

@bot.message_handler(func = lambda msg: isMessageHandler(msg.text))
def handler(msg):

    messageHandler = MessageHandler(bot)
    messageHandler.handle(msg)


@bot.message_handler(func = lambda msg: isDateHandler(msg.text))
def handler(msg):

    dataHandler = DateHandler(bot)
    dataHandler.handle(msg)


@bot.callback_query_handler(func = lambda call: isQueryHandler(call.data.split(':')[0]))
def handler(call):

    queryHandler = QueryHandler(bot)
    queryHandler.handle(call)


@bot.message_handler(func = lambda msg: msg.text.lower().find("/r") != -1)
def f(msg):

    command(bot, msg)


bot.infinity_polling(timeout = 10, long_polling_timeout = 5)

