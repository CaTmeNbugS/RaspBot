from modules.keyboard import keyboard
from modules.dates    import weekFull
from modules.shedule  import Shedule
from modules.db       import DataBase

import json

def getUserInfo(msg):

    userInfo = {
        'id':  msg.from_user.id,
        'username':  msg.from_user.username,
    }

    return json.dumps(userInfo)

def sendShedule(bot, msg, dates: list[str]) -> None:

    dataBase = DataBase('users')
    user     = dataBase.getUser(msg.from_user.id)

    if bool(user):

        sendMsg = ''

        for date in dates:
            
            shedule  = Shedule(date = date.strftime('%d-%m-%Y'), userType = user[2], userGroup = user[3])
            sendMsg += f'<b>{weekFull[date.weekday()]}:</b>\n{shedule.getMsgShedule()}\n'

        bot.send_message(msg.chat.id, sendMsg, reply_markup = keyboard(), parse_mode='HTML')

    else:

        bot.send_message(msg.chat.id, 'Я не нашел тебя. Напиши /start для повторной регистрации')

def sendComShedule(bot, msg, data: dict[str, str]) -> None:

    sendMsg = ''

    for date in data['dates']:
            
        shedule  = Shedule(date = date, userType = data['type'], userGroup = data['group'])
        sendMsg += f'{shedule.getMsgShedule()}\n'

    bot.send_message(msg.chat.id, sendMsg, reply_markup = keyboard(), parse_mode='HTML')