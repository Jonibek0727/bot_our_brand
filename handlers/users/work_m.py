from aiogram import types
from loader import dp
from keyboards.default.work_money import work_btn
from keyboards.default.startmenu import menuStart

@dp.message_handler(text = "🤑 Pul Ishlash")
async def bot_help(message: types.Message):
    
    
    await message.answer("Pul ishlash 🤑", reply_markup=work_btn)


@dp.message_handler(text = "🔙 Go Back")
async def bot_help(message: types.Message):
    
    
    await message.answer("Main Menu", reply_markup=menuStart)


@dp.message_handler(text = "👥 Do'stalrni taklif qilish")
async def bot_help(message: types.Message):
    
    
    await message.answer("""📎 Ushbu referal linkini do'stlaringizga yuboring 👉\nhttps://t.me/paynetbot?refllink216294947\n
🤖 Botdan ro'yxatdan o'tgan har bir do'stingiz uchun sizga: 250 so'm to'lanadi\n

💸 Pullaringizni paynet orqali telefon raqamingizga yoki kartangizga yechib olishingiz mumkin""")




@dp.message_handler(text = "📲 Vazifa bajarish")
async def bot_help(message: types.Message):
    
    
    await message.answer("📲 Internetda vazifa bajarib pul ishlash")
