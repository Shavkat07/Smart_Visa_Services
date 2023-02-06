from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboard_button import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Assalomu aleykum hurmatli mijoz {message.from_user.full_name}\n Smart visa botimizga xush kelibsiz!\n"
        f"Qiziqtirgan bo'limni tanlang.", reply_markup=menu)
