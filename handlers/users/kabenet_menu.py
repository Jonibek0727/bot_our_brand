from aiogram import types
from loader import dp
from keyboards.default.balans_btn import balns_btn

@dp.message_handler(text = "👤 Shaxsiy Kabinet")
async def bot_help(message: types.Message):
    
    
    await message.answer("""👤 Shaxsiy Kabinet

Assalomu alaykum (Foydalanuvchi niki) 

✅ Ismingiz: Ism 
✅ Jinsingiz: Jins
✅ Yoshingiz: Yosh 
✅ Manzil: Manzil
✅ Tel nomeringiz: nomer

👥 Do'stlaringiz: **** ta
📎 Shaxsiy referal linkingiz: https://t.me/paynetbot?reflink216274368""")