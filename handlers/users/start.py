from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startmenu import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum Hurmatli {message.from_user.full_name}!\nBotga Hushs kelibsiz", reply_markup=menuStart)
