import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values
import random

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher(bot)

unique_users = set()
names = ("Манас", "Жанат", "Аяна", "Дима", "Артем")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user = message.from_user
    unique_users.add(user.id)
    await message.answer(f"Привет, {user.first_name}! Наш бот обслуживает уже {len(unique_users)} пользователя(ей).")


@dp.message_handler(commands=['myinfo'])
async def myinfo_handler(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Ваш ID: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваш username: @{user.username if user.username else 'отсутствует'}"
    )


@dp.message_handler(commands=['random'])
async def random_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())