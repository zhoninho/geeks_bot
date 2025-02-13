from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from bot_config import database


# FSM - finite state machine
class RestourantReview(StatesGroup):
    name = State()
    contact = State()
    rate = State()
    text = State()


async def start_dialog(callback: CallbackQuery):
    await RestourantReview.name.set()
    await callback.message.answer("Как вас зовут?")


async def stop_dialog(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Спасибо за потраченное время")


async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await RestourantReview.next()
    await message.answer("Ваш номер телефона или инстаграм (укажите один из вариантов):")


async def process_contact(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
    await RestourantReview.next()
    await message.answer("Поставьте нам оценку от 1 до 5:")


async def process_rate(message: Message, state: FSMContext):
    rate = int(message.text)
    if not message.text.isdigit() or not (1 <= rate <= 5):
        await message.answer("Пожалуйста, введите число от 1 до 5.")
        return
    async with state.proxy() as data:
        data["rate"] = rate
    await RestourantReview.next()
    await message.answer("Дополнительные комментарии или жалоба (можете написать что угодно):")


async def process_text(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text
    await message.answer("Спасибо за отзыв!")
    data = await state.get_data()
    database.add_review(data)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == "feedback")
    dp.register_message_handler(
        stop_dialog, Text(equals=("стоп", "stop"), ignore_case=True), state="*"
    )
    dp.register_message_handler(process_name, state=RestourantReview.name)
    dp.register_message_handler(process_contact, state=RestourantReview.contact)
    dp.register_message_handler(process_rate, state=RestourantReview.rate)
    dp.register_message_handler(process_text, state=RestourantReview.text)
