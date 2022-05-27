from aiogram import types
from loader import dp
from keyboards.default.clik_pay import clik_btn

@dp.message_handler(text = "📤 Pulni yechib olish")
async def bot_help(message: types.Message):
    
    
    await message.answer("👇 To'lov turini tanlang", reply_markup=clik_btn)


@dp.message_handler(text = "💳 Click")
async def bot_help(message: types.Message):
    
    
    await message.answer("""Click raqamingiz: 0000 0000 0000 0000

Agar boshqa kartaga pul yechmoqchi bo'lsangiz /sozlash bo'limidan karta raqamini o'zgartiring""")
    


@dp.message_handler(text = "🟢 Paynet")
async def bot_help(message: types.Message):
    
    
    await message.answer("""Paynet uchun tel nomeringiz: +998*****

Agar boshqa nomerga pul yechmoqchi bo'lsangiz /sozlash bo'limidan nomerni o'zgartiring""")
