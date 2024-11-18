from Commandlet_Shedule import SheduleCommandlet

from functions.Dates    import getWeekDates, dateCalc
from functions.Handler  import Handler

from datetime import datetime
from datetime import timedelta

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

    def handle(self, msg):
    
        sheduleCommandlet = SheduleCommandlet(self.bot, msg)
        sheduleCommandlet.send(self.handlers[msg.text])

