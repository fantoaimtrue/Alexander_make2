import logging

from aiogram.utils.executor import start_webhook
from pyngrok import ngrok

from data.config import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_URL, \
    http_tunnel
from loader import bot


async def on_startup(dp):
    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)

    # print('Удаление БД')
    # await db.gino.drop_all()

    print('Создание таблиц')
    await db.gino.create_all()

    print('Готово')

    # from utils.notify_admins import on_startup_notify
    # await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print('Bot was started')

    # На webhook (ngrok)
    await bot.set_webhook(WEBHOOK_URL)


# Остановка бота
async def on_shutdown(dp):
    # delete webhook
    await bot.delete_webhook()
    ngrok.disconnect(http_tunnel.public_url)

    logging.warning('Shutting down..')
    logging.warning('Bye!')


if __name__ == "__main__":
    from handlers import dp

    # На webhook (ngrok)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
