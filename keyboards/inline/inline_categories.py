from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_datas import buy_callback
from testlen import updage
from databaseoutbut.get_info_form_db import get_categories,get_sostav,get_names
from django.contrib.admin.utils import flatten



def keyboard_categories():
    inline_kb = InlineKeyboardMarkup(row_width=2)
    categories = flatten(set(get_categories()))
    for keys in categories:
        inline_kb.row(InlineKeyboardButton(keys, callback_data=buy_callback.new(item_name=keys)))
    return inline_kb


def keyboard_names(category):
    inline_kb = InlineKeyboardMarkup(row_width=2)
    categories = flatten(set(get_sostav(category)))
    for keys in categories:
        inline_kb.row(InlineKeyboardButton(keys, callback_data=buy_callback.new(item_name=keys)))
    return inline_kb


# def key():
#
#     updage()
#     for items in updage():
#         inline_kb.row(InlineKeyboardButton(items, callback_data=buy_callback.new(item_name=items)))
#     return inline_kb

