from aiogram import types
from loader import dp
from keyboards.default.hisob_btn import Hisob_btn

@dp.message_handler(text = "💳 Hisob raqamni almashtirish")
async def bot_help(message: types.Message):
    
    
    await message.answer("💳 Hisob raqamni almashtirish", reply_markup=Hisob_btn)


@dp.message_handler(text = "💳 Click raqamini o'zgartirish")
async def bot_help(message: types.Message):
    
    
    await message.answer("Yangi click raqamini kiriting:")


@dp.message_handler(text = "📞 Tel nomerni o'zgartirish")
async def bot_help(message: types.Message):
    
    
    await message.answer("📞 Yangi tel nomer kiriting:")


