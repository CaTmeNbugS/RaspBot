from modules.Shedule    import findGroup
from modules.DataBase   import DataBase

from functions.Misc     import getUserInfo
from functions.Keyboard import keyboard, inlineKeyboardUserType

import logging
import json

class RegisterCommandlet:

    def __init__(self, bot):

        self.bot = bot


    def start(self, msg):

        self.bot.send_message(msg.chat.id, '*Разработчик*: `Кандаленцев Михаил`\n*Репозиторий*: `https://github.com/CaTmeNbugS/RaspBot`\n*Версия*: `1.3`', parse_mode='Markdown')
        self.bot.send_message(msg.chat.id, f'Привет, <b>{msg.from_user.first_name}</b>! Введи некоторые данные о себе\nТы в любой момент можешь их изменить написав /start', parse_mode='HTML')

        logging.info(f'{getUserInfo(msg)} start register')

        self.bot.send_message(msg.chat.id, 'Ты <b>студент</b> или <b>преподаватель</b>?', reply_markup = inlineKeyboardUserType(), parse_mode='HTML')
        self.bot.register_next_step_handler(msg, self.saveGroup)

    def saveGroup(self,msg):

        dataBase = DataBase('users')
        type     = dataBase.getUser(msg.from_user.id)[2]
        group    = findGroup(type, msg.text)

        if bool(group):

            dataBase.updateUser({'id':  msg.from_user.id, 'dataName': 'groupName', 'data': group})

            self.bot.send_message(msg.chat.id, "🎉 <b>Все готово!</b> 🎉", reply_markup = keyboard(), parse_mode='HTML')
            self.bot.send_message(msg.chat.id, "<blockquote><b>Нажимай</b> снизу на <b>кнопочки</b> и смотри расписание</blockquote>\n<blockquote><b>Кнопочки</b> <b><i>⬅ Неделя и Неделя ➡️</i></b> выводят расписание на <i>прошлую и следующую</i> недельку соответственно</blockquote>\n<blockquote>Еще у меня есть <b>команда /r</b>, напиши ее, чтобы узнать про нее</blockquote>\n<blockquote><b>Всего тебе хорошего! 😉</b></blockquote>", reply_markup=keyboard(), parse_mode='HTML')

            logging.info(f'{getUserInfo(msg)} successfully registered')

        else:

            self.bot.send_message(msg.chat.id, "<b>Извини</b>, но я ничего не нашел 🥺", parse_mode='HTML')
            self.bot.send_message(msg.chat.id, "Если ты студент - напиши вот в таком формате: <b>23ИСП-3</b>\n❗️ Без пробелов, номер группы писать через тире(-) ❗️", parse_mode='HTML')
            self.bot.send_message(msg.chat.id, "Если ты преподаватель - напиши <b> свою фамилию</b>", parse_mode='HTML')

            logging.warning(f'{getUserInfo(msg)} entered the group incorrectly ({json.dumps(msg.text)})')

            self.bot.register_next_step_handler(msg, self.saveGroup)
