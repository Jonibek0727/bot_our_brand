from aiogram import types
from loader import dp
from keyboards.default.balans_btn import balns_btn

@dp.message_handler(text = "📋 Qoidalar")
async def bot_help(message: types.Message):
    
    
    await message.answer("👮‍♂ Qoidalar")
