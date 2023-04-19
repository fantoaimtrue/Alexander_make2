from aiogram import types

from keyboards.main_menu import main_menu
from loader import dp
from utils.db_api import quick_commands as commands


### /start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        user = await commands.select_users(message.from_user.id)
        if user.status == 'active':
            text_1 = "Добро пожаловать в наш автоматизированный агрегатор!"
            await message.answer(f'{text_1}',
                                 reply_markup=main_menu())

    except Exception:
        text_2 = "Добро пожаловать в наш автоматизированный агрегатор! Здесь вы получите помощь в получении быстрого онлайн займа, потребуется лишь телефон или компьютер. Внимание, мы не осуществляем выдачу денег. Мы лишь анализируем и предлагаем вам лучшие возможности в этой сфере и не берем никаких комиссий. \n\n" \
                 "Если вы хотите ознакомиться со всеми предложениями переходите в раздел “Все займы” - всегда только актуальная информация.\n" \
                 "При нажатии на кнопку “Получить займ” вас отправит на соответствующий официальный сайт выбранной микрофинансовой организации.\n" \
                 "Если вы просто хотите увидеть лучшие предложения переходите в раздел “ТОП-5”, там мы указываем лучшие офферы с высоким процентом одобрений и хорошими условиями получения.\n" \
                 "В разделе “Рекомендации” вы найдете полезную информацию. Стоит ознакомиться. Прежде чем брать займы лучше понимать что это такое и как устроено.\n" \
                 "В разделе “Уведомления” вы можете отписаться от получения уведомлений от нас. Если для вас актуальны предложения по займам то мы не советуем отключать. По умолчанию мы уведомляем вас о наличии интересных акций и предложений.\n\n" \
                 "Надеемся, что наш сервис будет вам полезен. Данный чат-бот всегда у вас под рукой 24 на 7 :) Подбор Займа в телеграмме - Всегда под рукой FindCredit"
        await message.answer(f'{text_2}',
                             reply_markup=main_menu())
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
