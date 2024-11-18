from modules.DataBase   import DataBase
from modules.marks      import login, getMarks

from functions.Keyboard import keyboard, registerKeyboard
from functions.Misc     import getUserInfo

import logging

class MarksCommandlet:

    def __init__(self, bot, msg):
        
        self.bot = bot
        self.msg = msg

    def get(self):

        try:

            dataBase = DataBase('marks')
            user     = dataBase.getUser(self.msg.from_user.id)
            auth     = user[4] if bool(user) else '0'

            if bool(user) & (auth == '1'):

                logging.info(f'{getUserInfo(self.msg)} getting marks')

                self.bot.send_message(self.msg.chat.id, "🌀 <b>Подключаюсь к дневнику</b> 🌀", reply_markup = keyboard(), parse_mode='HTML')

                username = user[2]
                userpass = user[3]

                connect = login(username, userpass)

                if connect[0]:

                    self.bot.send_message(self.msg.chat.id, "⬇️ <b>Получаю твои оценки</b> ⬇️", reply_markup = keyboard(), parse_mode='HTML')

                    cookies = connect[1]
                    
                    username_  = cookies['USERNAME']
                    session_id = cookies['SESSION_ID']
                    curr_uch   = cookies['CURR_UCH']
                    uch        = cookies['UCH']

                    self.bot.send_message(self.msg.chat.id, "🙏 <b>Пожалуйста подожди</b> 🙏", reply_markup = keyboard(), parse_mode='HTML')

                    marks = getMarks(username_, session_id, curr_uch, uch)
                    
                    if marks[0]:

                        message = f'<blockquote><b>{username}</b></blockquote>\n—————————————————————————'

                        for subject in marks[1]:

                            marksMessage = ''
                            subjectHeader = ''

                            if len(subject['subjectName']) > 30:
                                
                                subjectHeader = subject['subjectName'][0:28] + '..'

                            else:

                                subjectHeader = subject['subjectName'] + (' ' * (30 - len(subject['subjectName'])))

                            for i, mark in enumerate(subject['marks']):

                                if(i % 16 == 0) & (i != 0):

                                    marksMessage += f' {mark}⠀\n'

                                else:

                                    marksMessage += f' {mark}'

                            if len(marksMessage) < 35:

                                marksMessage += f'{" " * (34 - len(marksMessage))}⠀'

                            message += f'<pre>{subjectHeader} {subject['grade']}</pre>\n<pre>{marksMessage}</pre>\n—————————————————————————'

                        self.bot.send_message(self.msg.chat.id, message, reply_markup = keyboard(), parse_mode='HTML')

                        logging.info(f'{getUserInfo(self.msg)} successfully get marks')

                    elif not marks[0]:

                        self.bot.send_message(self.msg.chat.id, marks[1], reply_markup = keyboard(), parse_mode='HTML')
                        logging.info(f'{getUserInfo(self.msg)} jornal error')
                
                elif not connect[0]:

                    self.bot.send_message(self.msg.chat.id, connect[1], reply_markup = keyboard(), parse_mode='HTML')
                    logging.info(f'{getUserInfo(self.msg)} authorized error')

            else:

                self.bot.send_message(self.msg.chat.id, "Чтобы смотреть оценки, нужно ввести <b>ЛОГИН</b> и <b>ПАРОЛЬ</b> от электронного дневника (journal.uc.osu.ru)", reply_markup = registerKeyboard(), parse_mode='HTML')
                self.bot.send_message(self.msg.chat.id, "Чтобы зарегестрироваться напиши <pre>Регистрация</pre>", reply_markup = registerKeyboard(), parse_mode='HTML')

        except:

            self.bot.send_message(self.msg.chat.id, "Что-то пошло не так 🙄", reply_markup = keyboard(), parse_mode='HTML')
