from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message,ReplyKeyboardRemove
from loader import dp
from  keyboards.defalt import menu


@dp.message_handler(Command("menu"))
async def show_menu(message:Message):
    await message.answer("Chooose one",reply_markup=menu)

@dp.message_handler(Text(equals=["Mugalim omirbayany","Mugalim jetistikteri","mugalim zertteyleri"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}.Thanks", reply_markup=ReplyKeyboardRemove())
