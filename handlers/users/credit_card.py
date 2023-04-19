from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.back_button import back_button
from loader import dp
from utils.db_api.quick_commands import count_card, select_card_9, \
    select_card_all


@dp.message_handler(text='Кредитные карты')
async def echo_message(message: types.Message):
    if message.text == 'Кредитные карты':
        # определяем количество записей с картами
        card_count = await count_card()
        if card_count > 9:
            card = await select_card_9(offset=0)
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in card:
                ikb.insert(
                    InlineKeyboardButton(str(o[1]),
                                         callback_data='opencard-' +
                                                       str(o[0])))
        else:
            card = await select_card_all()
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in card:
                ikb.insert(
                    InlineKeyboardButton(str(o[1]),
                                         callback_data='opencard-' +
                                                       str(o[0])))

        if card_count > 9:
            ikb.row(back_button('start'),
                    InlineKeyboardButton('➡️', callback_data='cardpage-2'))
        else:
            ikb.row(back_button('start'))

        await message.answer('Наши карты',
                             reply_markup=ikb)
