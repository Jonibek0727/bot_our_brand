from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Hisob_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="💳 Click raqamini o'zgartirish"),
           
        ],
        [
            KeyboardButton(text="📞 Tel nomerni o'zgartirish"),
           
        ],
        [
            KeyboardButton(text='🔙 Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)