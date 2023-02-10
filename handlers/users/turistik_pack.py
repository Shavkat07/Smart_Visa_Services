from aiogram import types
from keyboards.inline import turistic_pack_dav

from loader import dp, bot

import logging

logging.basicConfig(level=logging.INFO)


@dp.message_handler(text="Turistik paketlar")
async def tur_paket(message: types.Message):
    await message.answer("Davlatni tanlang:", reply_markup=turistic_pack_dav.tur_dav)



