import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.newpost import NewPost


@dp.message_handler(Command("post"))
async def create_post(message: Message):
    await message.answer("Kanalg'a shig'ariw ushin post jiberin'.")
    await message.answer(""" To'mendegishe:
Лауазым: Программист
Мекеме: АралГолд
Мәнзил: Нөкис
Талаплар: Фотошоп корелдрау билиу керек.
Мәжбурияты: Жумста принтер оңлауы керек, қағазды тусну керек код жазуы керек
Жумыс уақты: 9:00 - 18:00
Жумыс шараяты: 
уютный офис в центре г.Нукус
Кофе яай плистишн
Айлық: 300$
Байланыс: 99188389301
Телеграм: @лвлвбы
Қосымша: Турмсқа шықпаған сулу қызлар керек айтеуир куйеуи жоқ болса болды""")
    await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Postti tekseriw ushin jibereyinba?",
                         reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post Adminge jiberildi")
    await bot.send_message(ADMINS[0], f"Paydalaniwshi  {mention} tomendegishe postti qoyajaq:")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post qoyilmadi.")


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: Message):
    await message.answer("Kanalg'a shig'ariwdi ya shig'armawdi saylan'")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Kanalg'a shig'ariwg'a ruxsat berdin'iz.", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("Post otkaz etildi.", show_alert=True)
    await call.message.edit_reply_markup()
