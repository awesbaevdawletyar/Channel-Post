from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyriqlar: ",
            "/start - Botti iske tusiriw",
            "/help - Help",
            "/post - postti kanalg'a shig'ariw")
    
    await message.answer("\n".join(text))