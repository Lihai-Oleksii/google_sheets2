from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_datas import buy_callback


inline_btn_1 = InlineKeyboardButton('Проектори', callback_data=buy_callback.new(item_name='proj'))
inline_btn_2 = InlineKeyboardButton("Комп'ютери", callback_data=buy_callback.new(item_name='pc'))
inline_btn_3 = InlineKeyboardButton('Ноутбуки', callback_data=buy_callback.new(item_name='notebook'))
inline_btn_4 = InlineKeyboardButton('Принтеры', callback_data=buy_callback.new(item_name='printer'))
inline_btn_5 = InlineKeyboardButton('Картриджі', callback_data=buy_callback.new(item_name='catr'))                  #   Создаем кнопки
inline_btn_6 = InlineKeyboardButton('Телефонна Технiка', callback_data=buy_callback.new(item_name='teleteh'))
inline_btn_7 = InlineKeyboardButton('Екрани', callback_data=buy_callback.new(item_name='ekran'))
inline_btn_8 = InlineKeyboardButton('Сканери', callback_data=buy_callback.new(item_name='skaner'))
inline_btn_9 = InlineKeyboardButton('Шредери', callback_data=buy_callback.new(item_name='shreder'))
inline_btn_10 = InlineKeyboardButton('Витратні матеріали для принтерів',
                                               callback_data=buy_callback.new(item_name='rashod'))
inline_kb1 = InlineKeyboardMarkup(row_width=2).add(inline_btn_1,inline_btn_2,inline_btn_3,inline_btn_4,inline_btn_5,                #  Добавляем их в клавиатуру
                                        inline_btn_6,inline_btn_7,inline_btn_8,inline_btn_9,inline_btn_10)                          


def key_board_price(p,p2,p3):
    inline_price_1 = InlineKeyboardButton(p, callback_data=buy_callback.new(item_name='100-1000'))
    inline_price_2 = InlineKeyboardButton(p2, callback_data=buy_callback.new(item_name='1000-2000'))
    inline_price_3 = InlineKeyboardButton(p3, callback_data=buy_callback.new(item_name='2000-4500'))                        #   Функция, чтобы вызывать её в хендлерах с задаными параметрами
    inline_price_all = InlineKeyboardButton('Усi товари', callback_data=buy_callback.new(item_name='all'))
    inline_price_full = InlineKeyboardMarkup(row_width=2)
    inline_price_full.add(inline_price_1,inline_price_2,inline_price_3,inline_price_all)
    return inline_price_full



