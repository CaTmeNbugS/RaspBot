from modules.Shedule    import Shedule, findGroup

from functions.Misc     import getUserInfo
from functions.Keyboard import keyboard

import logging

def command(bot, msg):

    logging.info(f'{getUserInfo(msg)} get com')

    args = msg.text.split(' ')

    if (len(args) >= 4) & (len(args) <= 5):

        type = '1' if (args[1].lower() == 'с') | (args[1].lower() == 'c') else '2'
        group = findGroup(type, args[2])

        if bool(group):

            sendMsg = ''

            for date in [args[3]]:
            
                shedule  = Shedule(date = date, userType = type, userGroup = group)
                sendMsg += f'{shedule.getMsgShedule()}\n'

            bot.send_message(msg.chat.id, sendMsg, reply_markup = keyboard(), parse_mode='HTML')
        
        else:

            bot.send_message(msg.chat.id, f'Кажется, ты не правильно ввел {'название группы' if type == '1' else 'фамилию преподавателя'} 🤓' , parse_mode='HTML', reply_markup=keyboard())

    else:

        bot.send_message(msg.chat.id, '<b>Как пользоваться командой /r?</b><blockquote><b>1</b> - Пиши <b>студент</b> или <b>преподаватель</b>\n <i>c - если студент</i> | <i>п - если преподаватель</i></blockquote>\n<blockquote><b>2</b> - Пиши <b>название</b> группы или <b>фамилию</b> преподавателя</blockquote>\n<blockquote><b>3</b> - Пиши число в формате <b>00-00-0000</b></blockquote>\n<pre>/r с 23ИСП-3 27-09-2024</pre>', parse_mode='HTML', reply_markup=keyboard())
