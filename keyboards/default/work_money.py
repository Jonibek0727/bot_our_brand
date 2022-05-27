from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

work_btn = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👥 Do'stalrni taklif qilish"),
           
        ],
        [
            KeyboardButton(text='📲 Vazifa bajarish'),
           
        ],
        [
            KeyboardButton(text='🔙 Go Back'),
           
        ],
       
    ],
    resize_keyboard=True
)