from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# main menu
def main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.row('Все займы', KeyboardButton('Топ 5'))
    return kb
