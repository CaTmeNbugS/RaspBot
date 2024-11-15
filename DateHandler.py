from modules.dates       import getWeekDates, dateCalc
from modules.sendShedule import sendShedule, getUserInfo
from modules.handler     import Handler

from datetime import datetime
from datetime import timedelta

import logging

@Handler
def isDateHandler():
    return ['⬅ Неделя', 'Неделя', 'Неделя ➡️', 'Сегодня', 'Завтра', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Су']

class DateHandler:

    def __init__(self, bot):

        self.bot = bot
        self.handlers = {
            '⬅ Неделя': getWeekDates(datetime.today() - timedelta(weeks = 1)),
            'Неделя':    getWeekDates(datetime.today()),
            'Неделя ➡️': getWeekDates(datetime.today() + timedelta(weeks = 1)),
            'Сегодня':   [datetime.today()],
            'Завтра':    [datetime.today() + timedelta(days = 1)],
            'Пн':        [dateCalc(datetime.today(), 'Пн')],
            'Вт':        [dateCalc(datetime.today(), 'Вт')],
            'Ср':        [dateCalc(datetime.today(), 'Ср')],
            'Чт':        [dateCalc(datetime.today(), 'Чт')],
            'Пт':        [dateCalc(datetime.today(), 'Пт')],
            'Су':        [dateCalc(datetime.today(), 'Су')]
        }
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

    def handle(self, msg):
    
        logging.info(f'{getUserInfo(msg)} get {self.logs[msg.text]}')

        sendShedule(self.bot, msg, self.handlers[msg.text])
