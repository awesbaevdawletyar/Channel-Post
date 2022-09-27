from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botti iske tu'siriw"),
            types.BotCommand("help", "Ja'rdem"),
            types.BotCommand("post", "Kanalg'a shig'ariw"),
        ]
    )
