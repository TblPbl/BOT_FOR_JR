from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

import os
import asyncio

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message()
async def all_messages(message: Message):
    await message.answer(
        text=f'Здорово {message.from_user.full_name}'
    )


async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start_bot())
