from aiogram import types
from loader import dp
from keyboards.default.balans_btn import balns_btn

@dp.message_handler(text = "💰 Balans")
async def bot_help(message: types.Message):
    
    
    await message.answer("Balans 🤑")
    await message.answer("""💰Sizning hisobingizda: **** so'm mavjud

💵 Umumiy ishlagan pullaringiz: **** so'm 
💸 Yechib oldingiz: **** so'm 

💳 Sizning karta raqamingiz: karta raqam
📞 Paynet uchun tel nomeringiz: tel nomer""", reply_markup=balns_btn)