from aiogram import types
from aiogram.types import InlineKeyboardButton


def back_button(url, single=False):
    if single == True:
        return types.InlineKeyboardMarkup(row_width=1).row(
            InlineKeyboardButton('<<< Назад', callback_data=url))
    else:
        return InlineKeyboardButton('ГЛ. МЕНЮ', callback_data=url)
