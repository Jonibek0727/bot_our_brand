from aiogram import types
from matplotlib.pyplot import text
from loader import dp
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.setting_btn import sett_btn


@dp.message_handler(Command("sozlash"))
async def bot_help(message: types.Message):
    
    
    await message.answer("⚙️ Sozlash", reply_markup=sett_btn)


@dp.message_handler(text = '⚙️ Shozlash')
async def bot_help(message: types.Message):
    
    
    await message.answer("⚙️ Sozlash", reply_markup=sett_btn)
