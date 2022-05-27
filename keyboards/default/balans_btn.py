from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balns_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📤 Pulni yechib olish"),
           
        ],
        
        [
            KeyboardButton(text='🔙 Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)