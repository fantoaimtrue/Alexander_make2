import logging
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.back_button import back_button
from keyboards.main_menu import main_menu
from loader import dp
from utils.db_api.quick_commands import select_table_all, select_table_9, \
    select_count, select_offer


@dp.message_handler(text='Все займы')
async def all_loan(message: types.Message):
    try:
        offer_count = await select_count()
        if offer_count > 9:
            offer = await select_table_9(offset=0)
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(
                    InlineKeyboardButton(str(o[1]),
                                         callback_data='openoffer-' + str(o[0]))
                )
            ikb.row(back_button('start'),
                    InlineKeyboardButton('➡️', callback_data='offerpage-2'))
            await message.answer('Актуальные предложения по кредитным картам '
                                 'от известных банков.', reply_markup=ikb)
        else:
            offer = await select_table_all()
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(
                    InlineKeyboardButton(str(o[1]),
                                         callback_data='openoffer-' + str(o[0]))
                )
            await message.answer('Актуальные предложения по кредитным картам '
                                 'от известных банков.', reply_markup=ikb)
    except Exception as ex:
        print(ex)


@dp.callback_query_handler(lambda c: c.data)
async def all_loan_callback(callback: types.CallbackQuery):
    try:
        await callback.answer()
    except:
        logging.warning('ошибка при ответе на кнопку пользователя')
    get = callback.data

    if get == 'start':
        await callback.message.delete()
        await callback.message.answer('Главное меню', reply_markup=main_menu())

    if 'offerpage' in get:
        data = get.split('-')
        offer_count = await select_count()

        page_size = 9
        offset = (page_size * (int(data[1]) - 1))
        offer = await select_table_9(offset=offset)
        if 9 <= offset < offer_count:
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(InlineKeyboardButton(
                    str(o[1]), callback_data='openoffer-' + str(o[0])
                ))
            ikb.row(
                InlineKeyboardButton('⬅️', callback_data='offerpage-' + str(
                    int(data[1]) - 1)),
                back_button('start'),
                InlineKeyboardButton('➡️', callback_data='offerpage-' + str(
                    int(data[1]) + 1))
            )
            await callback.message.edit_reply_markup(reply_markup=ikb)
        elif offset == 0:
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(InlineKeyboardButton(
                    str(o[1]), callback_data='openoffer-' + str(o[0])
                ))
            ikb.row(
                back_button('start'),
                InlineKeyboardButton('➡️', callback_data='offerpage-' + str(
                    int(data[1]) + 1))
            )
            await callback.message.edit_reply_markup(reply_markup=ikb)
        elif offer_count > offset + page_size:
            print('hi')
        else:
            offer = await select_table_9(offset=0)
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(
                    InlineKeyboardButton(str(o[1]),
                                         callback_data='openoffer-' + str(
                                             o[0])),
                )
                ikb.row(
                    back_button('start')
                )

        if offer_count >= offset > offer_count - page_size:
            offer = await select_table_9(offset=offset)
            ikb = InlineKeyboardMarkup(row_width=3)
            for o in offer:
                ikb.insert(InlineKeyboardButton(str(o[1]),
                                                callback_data='openoffer-' + str(
                                                    o[0])))
            ikb.row(
                InlineKeyboardButton('⬅️', callback_data='offerpage-' + str(
                    int(data[1]) - 1)),
                back_button('start')
            )
            await callback.message.edit_reply_markup(reply_markup=ikb)

    if 'openoffer' in get:
        data = get.split('-')
        offer_data = int(data[1])
        offer = await select_offer(offer_data=offer_data)
        ikb = types.InlineKeyboardMarkup().add(
            InlineKeyboardButton('Получить займ', url=offer[3]))
        if offer[5] != 'NULL':
            await callback.message.answer_photo(offer[5],
                                                offer[1] + '\n\n' + offer[2],
                                                reply_markup=ikb.row(
                                                    back_button('start')))
        else:
            await callback.message.answer(offer[1] + '\n\n' + offer[2],
                                          reply_markup=ikb.row(
                                              back_button('start')))
