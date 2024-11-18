from modules.Shedule    import Shedule
from modules.DataBase   import DataBase

from functions.Keyboard import keyboard
from functions.Dates    import weekFull
from functions.Misc     import getUserInfo

import logging

class SheduleCommandlet:

    def __init__(self, bot, msg):
        
        self.bot = bot
        self.msg = msg

        self.logs = {
            '⬅ Неделя': 'Last week',
            'Неделя':    'Current week',
            'Неделя ➡️': 'Next week',
            'Сегодня':   'Today',
            'Завтра':    'Tomorrow',
            'Пн':        'Monday',
            'Вт':        'Tuesday',
            'Ср':        'Wednesday',
            'Чт':        'Thursday',
            'Пт':        'Friday',
            'Су':        'Saturday'
        }  
    
    def send(self, dates):

        logging.info(f'{getUserInfo(self.msg)} get {self.logs[self.msg.text]}')

        dataBase = DataBase('users')
        user     = dataBase.getUser(self.msg.from_user.id)

        if bool(user):

            sendMsg = ''

            for date in dates:
            
                shedule  = Shedule(date = date.strftime('%d-%m-%Y'), userType = user[2], userGroup = user[3])
                sendMsg += f'<b>{weekFull[date.weekday()]}:</b>\n{shedule.getMsgShedule()}\n'

            self.bot.send_message(self.msg.chat.id, sendMsg, reply_markup = keyboard(), parse_mode='HTML')

        else:

            self.bot.send_message(self.msg.chat.id, 'Я не нашел тебя. Напиши /start для повторной регистрации')