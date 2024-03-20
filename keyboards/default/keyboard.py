from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📑 Biz haqimizda'),
            KeyboardButton(text='📑 Normativ-huquqiy hujjatlar'),
        ],
        [
            KeyboardButton(text='📍 Manzil'),
            KeyboardButton(text='📨 Murojaatlar'),
        ],
    ],
    resize_keyboard=True
)

chek = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ha'),
            KeyboardButton(text="Yo'q"),
        ],
    ],
    resize_keyboard=True
)
