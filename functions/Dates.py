from datetime import datetime
from datetime import timedelta

week     = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Су']
weekFull = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

def dateCalc(today: datetime, name: str) -> datetime:

    weekMerge: int = week.index(name) - today.weekday()
    day: timedelta = timedelta(days = 1)

    return today + (weekMerge * day)

def getWeekDates(today: datetime) -> list[datetime]:

    dates: list[datetime] = []

    for day in week:

        date = dateCalc(today, day)
        dates.append(date)

    return dates

def isDayName(name: str) -> bool:

    for day in week:
        if name == day:
            return True

    return False 