from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Kanalg'a shig'ariw", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ Kanalg'a shig'armaw", callback_data=post_callback.new(action="cancel")),
    ]]
)
