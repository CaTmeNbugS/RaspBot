from modules.DataBase  import DataBase

from functions.Handler import Handler

@Handler
def isQueryHandler():
    return ['changeUserType']

class QueryHandler:

    def __init__(self, bot):
        
        self.bot = bot
        self.handlers = {
            'changeUserType': self.changeUserType
        }

    def handle(self, call):

        data = call.data.split(':')

        query = data[0]
        param = data[1]

        self.handlers[query](call, param)

    def changeUserType(self, call, param):
        
        dataBase = DataBase('users')
        dataBase.createUser({'id': call.from_user.id, 'link': call.from_user.username})

        if param == 'student':

            dataBase.updateUser({'id': call.from_user.id, 'dataName': 'userType', 'data': '1'})
            self.bot.send_message(call.from_user.id, "Напиши название группы")

        elif param == 'teacher':

            dataBase.updateUser({'id': call.from_user.id, 'dataName': 'userType', 'data': '2'})
            self.bot.send_message(call.from_user.id, "Напиши свою фамилию")

