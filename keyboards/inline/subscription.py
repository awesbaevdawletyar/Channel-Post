from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Kanalg'a qosilg'anin tekseriw", callback_data="check_subs")
    ]]
)
