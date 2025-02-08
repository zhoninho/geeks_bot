import asyncio
from bot_config import dp
from handlers import start, other_message


async def main():
    start.register_handlers(dp)
    other_message.register_handlers(dp)
    await dp.start_polling(dp)


if __name__ == '__main__':
    asyncio.run(main())