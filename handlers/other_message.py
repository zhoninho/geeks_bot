from aiogram import Dispatcher, types
import random
from bot_config import names

async def myinfo_handler(message: types.Message):
    user = message.from_user
    await message.answer(
        f"Ваш ID: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваш username: @{user.username if user.username else 'отсутствует'}"
    )


async def random_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")


async def promo_handler(message: types.Message):
    await message.answer(
        "Наши текущие акции:\n"
        "Шаурма 2+1 — закажите две шаурмы и получите третью в подарок!\n"
        "Бесплатный напиток при заказе от 1000 сом.\n"
        "Акция действует до конца недели!"
    )


async def loyalty_handler(message: types.Message):
    await message.answer(
        "Наша программа лояльности:\n"
        "Каждый 10-й заказ — бесплатно!\n"
        "Скидка 10% на день рождения 🎂\n"
        "Кэшбэк 5% на все заказы в мобильном приложении."
    )


async def rush_hour_handler(message: types.Message):
    await message.answer(
        "Часы пик:\n"
        "12:00 - 14:00 (обеденный перерыв)\n"
        "18:00 - 21:00 (ужин и вечерний трафик)"
    )


async def other_handler(message: types.Message):
    await message.answer("Я вас не понимаю.")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(myinfo_handler, commands=['myinfo'])
    dp.register_message_handler(random_handler, commands=['random'])
    dp.register_message_handler(promo_handler, commands=["promo"])
    dp.register_message_handler(loyalty_handler, commands=["loyalty"])
    dp.register_message_handler(rush_hour_handler, commands=["rush_hour"])
    dp.register_message_handler(other_handler)