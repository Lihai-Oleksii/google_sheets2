from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Вторая кнопка!', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Третья кнопка!', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('Четвертая кнопка!', callback_data='button4')
inline_btn_5 = InlineKeyboardButton('Пятая кнопка!', callback_data='button')
inline_btn_6 = InlineKeyboardButton('Пятая кнопка!', callback_data='button6')
inline_btn_7 = InlineKeyboardButton('Пятая кнопка!', callback_data='button7')
inline_btn_8 = InlineKeyboardButton('Пятая кнопка!', callback_data='button8')
inline_btn_9 = InlineKeyboardButton('Пятая кнопка!', callback_data='button9')
inline_btn_10 = InlineKeyboardButton('Пятая кнопка!', callback_data='button10')


inline_kb1 = InlineKeyboardMarkup(row_width=2).add(inline_btn_1,inline_btn_2,inline_btn_3,inline_btn_4,inline_btn_5,
                                        inline_btn_6,inline_btn_7,inline_btn_8,inline_btn_9,inline_btn_10)




