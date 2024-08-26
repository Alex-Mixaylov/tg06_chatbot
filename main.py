import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp

import logging

import sqlite3

import os
from dotenv import load_dotenv


# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена телеграм-бота и API-ключа из переменных окружения
TOKEN = os.getenv('TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Настройка логирования
logging.basicConfig(level=logging.INFO)









async def main():
 await dp.start_polling(bot)

if __name__ == '__main__':
 asyncio.run(main())
