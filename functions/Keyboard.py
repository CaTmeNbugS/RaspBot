from telebot  import types

def keyboard():

    keyboard  = types.ReplyKeyboardMarkup(resize_keyboard=True)

    prevWeek  = types.KeyboardButton("⬅ Неделя")    
    week      = types.KeyboardButton("Неделя")
    nextWeek  = types.KeyboardButton("Неделя ➡️")
    keyboard.row(prevWeek, week, nextWeek)

    monday    = types.KeyboardButton("Пн")
    tuesday   = types.KeyboardButton("Вт")
    wednesday = types.KeyboardButton("Ср")
    thursday  = types.KeyboardButton("Чт")
    friday    = types.KeyboardButton("Пт")
    saturday  = types.KeyboardButton("Су")
    keyboard.row(monday, tuesday, wednesday, thursday, friday, saturday)

    today     = types.KeyboardButton("Сегодня")
    tomorrow  = types.KeyboardButton("Завтра")
    marks     = types.KeyboardButton("Оценки 📖")
    keyboard.row(today, tomorrow, marks)

    return keyboard

def inlineKeyboardUserType():
    
    keyboard = types.InlineKeyboardMarkup()

    student  = types.InlineKeyboardButton('Студент 🧑‍🎓', callback_data='changeUserType:student')
    teacher  = types.InlineKeyboardButton('Преподаватель 👨‍🏫', callback_data='changeUserType:teacher')
    keyboard.row(student, teacher)

    return keyboard

def registerKeyboard():

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    agree    = types.KeyboardButton("Регистрация")
    deny     = types.KeyboardButton("Отмена")
    keyboard.row(agree, deny)

    return keyboard
