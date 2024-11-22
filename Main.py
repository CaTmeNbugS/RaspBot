from Handler_Date    import DateHandler,    isDateHandler
from Handler_Query   import QueryHandler,   isQueryHandler
from Handler_Message import MessageHandler, isMessageHandler

from Commandlet_Command import command

from   Server import WebhookServer
import cherrypy

from   Config import bot
import Config

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


bot.remove_webhook()
bot.set_webhook(url = Config.WEBHOOK_URL_BASE + Config.WEBHOOK_URL_PATH, certificate = open(Config.WEBHOOK_SSL_CERT, 'r'))

cherrypy.quickstart(WebhookServer(), Config.WEBHOOK_URL_PATH, {'/': {}})


