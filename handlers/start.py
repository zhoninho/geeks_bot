from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def start_handler(message: types.Message):
    user = message.from_user
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Наш адрес', callback_data='address'),
            InlineKeyboardButton(text='Контакты', callback_data='contacts'),
        ],
        [
            InlineKeyboardButton(text='Наш сайт', url='https://maxexpresscargo.com/'),
            InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/max_burger_kg/'),
        ],
        [
            InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback'),
            InlineKeyboardButton(text='Наши вакансии', callback_data='vacancies'),
        ],
        [
            InlineKeyboardButton(text='Меню', callback_data='menu'),
            InlineKeyboardButton(text='Режим работы', callback_data='working schedule'),
        ],
        [
            InlineKeyboardButton(text='Доставка Яндекс', url='https://eda.yandex.ru/Bishkek'),
        ]
    ])
    await message.answer(f'Здравствуйте, {user.first_name}! Вас приветсвует бот Max_burger.kg', reply_markup=kb)
    await message.answer(f"ID: {user.id}")

async def address_handler(callback: CallbackQuery):
    await callback.message.answer('Наши филиалы в Бишкеке: \nКурманжан Датки, 254 \nГорького, 126 \nпроспект Чуй, 271')

async def contacts_handler(callback: CallbackQuery):
    await callback.message.answer('tel:+996705126126')

async def vacancies_handler(callback: CallbackQuery):
    await callback.message.answer(
        'У нас есть открытые вакансии! Напишите в директ: @max_burger_kg для консультации.')

async def menu_handler(callback: CallbackQuery):
    await callback.message.answer('Наше меню:\n1. Max бургер\n2. Шаурма\n3. Крылышки\n4. Макаронсы')

async def working_schedule_handler(callback: CallbackQuery):
    await callback.message.answer('24/7')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_callback_query_handler(address_handler, lambda c: c.data == 'address')
    dp.register_callback_query_handler(contacts_handler, lambda c: c.data == 'contacts')
    dp.register_callback_query_handler(vacancies_handler, lambda c: c.data == 'vacancies')
    dp.register_callback_query_handler(menu_handler, lambda c: c.data == 'menu')
    dp.register_callback_query_handler(working_schedule_handler, lambda c: c.data == 'working schedule')