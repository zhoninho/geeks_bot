from aiogram import executor
from bot_config import dp, database, ADMINS, bot
from handlers import start, other_message, review_dialog, store_fsm, send_products

from db.main_db import create_tables


async def on_startup(_):
    for admin in ADMINS:
        await bot.send_message(admin, "Bot activated!")

    await create_tables()

async def on_shutdown(_):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin,
                               text='Бот выключен!')

start.register_handlers(dp)
review_dialog.register_handlers(dp)
store_fsm.register_handlers(dp)
send_products.register_handlers(dp)
other_message.register_handlers(dp)
database.create_tables()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)