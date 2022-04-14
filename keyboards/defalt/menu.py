from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Mugalim omirbayany"),
        ],
        [
        KeyboardButton(text="Mugalim jetistikteri"),
        ],
        [
        KeyboardButton(text="mugalim zertteyleri "),
        ],
    ],
    resize_keyboard=True

)