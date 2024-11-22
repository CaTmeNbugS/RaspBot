import cherrypy
import telebot

from   Config import bot
import Config

class WebhookServer(object):

    @cherrypy.expose
    def index(self):

        if 'content-length' in cherrypy.request.headers and \
           'content-type'   in cherrypy.request.headers and \
            cherrypy.request.headers['content-type'] == 'application/json':

            length  = int(cherrypy.request.headers['content-length'])
            jsonStr = cherrypy.request.body.read(length).decode("utf-8")
            update  = telebot.types.Update.de_json(jsonStr)

            bot.process_new_updates([update])

            return ''
        else:

            raise cherrypy.HTTPError(403)
        
cherrypy.config.update({
    'server.socket_host': Config.WEBHOOK_LISTEN,
    'server.socket_port': Config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': Config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': Config.WEBHOOK_SSL_PRIV
})