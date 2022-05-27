from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sett_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="🇺🇿 Tilni tanlash"),
           
        ],
        [
            KeyboardButton(text='💳 Hisob raqamni almashtirish'),
           
        ],
        [
            KeyboardButton(text="👤 Shaxsiy ma'lumotlarni o'zgartirish"),
           
        ],
        [
            KeyboardButton(text='🔙 Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)