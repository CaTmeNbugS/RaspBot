from Commandlet_StartRegister import RegisterCommandlet
from Commandlet_MarksRegister import MarksRegisterCommandlet
from Commandlet_Marks         import MarksCommandlet

from functions.Handler        import Handler
from functions.Keyboard       import keyboard

@Handler
def isMessageHandler():
    return ['Оценки', 'Оценки 📖', 'оценки', 'Регистрация', 'регистрация', 'Отмена', 'отмена', '/start', 'start']

class MessageHandler:

    def __init__(self, bot):
        
        self.bot = bot
        self.handlers = {
            'Оценки':      self.getMarks,
            'Оценки 📖':  self.getMarks,
            'оценки':      self.getMarks,
            'Регистрация': self.marksRegistration,
            'регистрация': self.marksRegistration,
            'Отмена':      self.cancel,
            'отмена':      self.cancel,
            '/start':      self.startRegistration,
            'start':       self.startRegistration,
        }

    def handle(self, msg):
        
        self.handlers[msg.text](msg)

    def cancel(self, msg):

        self.bot.send_message(msg.chat.id, "Окей 😉", reply_markup = keyboard(), parse_mode='HTML')

    def marksRegistration(self, msg):

        register = MarksRegisterCommandlet(self.bot)
        register.start(msg)

    def startRegistration(self, msg):

        register = RegisterCommandlet(self.bot)
        register.start(msg)

    def getMarks(self, msg):
        
        marks = MarksCommandlet(self.bot, msg)
        marks.get()


    