from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

clik_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="💳 Click"),
           
        ],
        [
            KeyboardButton(text="🟢 Paynet"),
           
        ],
        
        [
            KeyboardButton(text='🔙 Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)