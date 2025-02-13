import asyncio
from bot_config import dp, database
from handlers import start, other_message, review_dialog


async def main():
    start.register_handlers(dp)
    review_dialog.register_handlers(dp)
    other_message.register_handlers(dp)
    database.create_tables()
    await dp.start_polling(dp)


if __name__ == '__main__':
    asyncio.run(main())