from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

sett_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="πΊπΏ Tilni tanlash"),
           
        ],
        [
            KeyboardButton(text='π³ Hisob raqamni almashtirish'),
           
        ],
        [
            KeyboardButton(text="π€ Shaxsiy ma'lumotlarni o'zgartirish"),
           
        ],
        [
            KeyboardButton(text='π Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)