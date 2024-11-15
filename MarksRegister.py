from modules.db       import DataBase
from modules.marks    import login
from modules.keyboard import keyboard, repeatRegisterKeyboard
from telebot          import types
from modules.sendShedule import getUserInfo

import logging

class MarksRegister:

    def __init__(self, bot):
        
        self.bot = bot

    
    def start(self, msg):

        logging.info(f'{getUserInfo(msg)} start mark register')

        self.bot.send_message(msg.chat.id, "Напиши <b>ЛОГИН</b>", reply_markup = types.ReplyKeyboardRemove(), parse_mode='HTML')

        self.bot.register_next_step_handler(msg, self.savePassword)
    
    def savePassword(self, msg):

        dataBase = DataBase('marks')

        dataBase.createUser({'id': msg.from_user.id, 'link': msg.from_user.username})
        dataBase.updateUser({'id': msg.from_user.id, 'dataName': 'USERNAME', 'data': msg.text})

        self.bot.send_message(msg.chat.id, "Напиши <b>ПАРОЛЬ</b>", reply_markup = types.ReplyKeyboardRemove(), parse_mode='HTML')

        self.bot.register_next_step_handler(msg, self.authorize)
    
    def authorize(self, msg):

        dataBase = DataBase('marks')
        dataBase.updateUser({'id': msg.from_user.id, 'dataName': 'USERPASS', 'data': msg.text})

        user     = dataBase.getUser(msg.from_user.id)
        username = user[2]
        userpass = user[3]

        session = login(username, userpass)

        if session[0] == True:

            logging.info(f'{getUserInfo(msg)} successfully authorized')

            dataBase.updateUser({'id': msg.from_user.id, 'dataName': 'authorized', 'data': '1'})
            self.bot.send_message(msg.chat.id, 'Готово! Можешь смотреть оценки', reply_markup = keyboard(), parse_mode='HTML')

        else:

            logging.info(f'{getUserInfo(msg)} unsuccessfully authorized')

            dataBase.updateUser({'id': msg.from_user.id, 'dataName': 'authorized', 'data': '0'})
            self.bot.send_message(msg.chat.id, session[1], reply_markup = repeatRegisterKeyboard(), parse_mode='HTML')
            self.bot.send_message(msg.chat.id, 'Попробуешь еще раз?', reply_markup = repeatRegisterKeyboard(), parse_mode='HTML')

