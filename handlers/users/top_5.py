from aiogram import types
from aiogram.types import InlineKeyboardButton

from loader import dp
from utils.db_api.quick_commands import select_top_5
from keyboards.back_button import back_button

@dp.message_handler(text=['Топ 5'])
async def top_5(message: types.Message):

    offer = await select_top_5()

    kb = types.InlineKeyboardMarkup(row_width=3)
    for o in offer:
        kb.row(
            InlineKeyboardButton(str(o[1]), callback_data='openoffer-' + str(o[0])))

    kb.row(back_button('start'))

    await message.answer('Топ лучших микрофинансовых организаций на сегодня (сведены все показатели оценки - одобряемость займа, выгодность условий для клиента, суммы выдачи, удобство при первом обращении и многое другое)', reply_markup=kb)