from aiogram import types
from loader import dp
from keyboards.default.balans_btn import balns_btn

@dp.message_handler(text = "๐ฐ Balans")
async def bot_help(message: types.Message):
    
    
    await message.answer("Balans ๐ค")
    await message.answer("""๐ฐSizning hisobingizda: **** so'm mavjud

๐ต Umumiy ishlagan pullaringiz: **** so'm 
๐ธ Yechib oldingiz: **** so'm 

๐ณ Sizning karta raqamingiz: karta raqam
๐ Paynet uchun tel nomeringiz: tel nomer""", reply_markup=balns_btn)