from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🤑 Pul Ishlash'),
           
        ],
         [
            KeyboardButton(text='💰 Balans'),
            KeyboardButton(text='👤 Shaxsiy Kabinet'),
           
        ],
         [
            KeyboardButton(text='📋 Qoidalar'),
            KeyboardButton(text="🧑‍💻 Bog'lanish"),
           
        ],
         [
            KeyboardButton(text='⚙️ Shozlash'),
           
        ],
    ],
    resize_keyboard=True
)