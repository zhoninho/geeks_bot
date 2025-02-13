from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import Database


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
storage = MemoryStorage()
database = Database("database.sqlite3")
dp = Dispatcher(bot, storage=storage)

names = ("Манас", "Жанат", "Аяна", "Дима", "Артем")