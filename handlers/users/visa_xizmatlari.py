from aiogram import types
from keyboards.default.keyboard_button import menu, visa_xizmatlari
from keyboards.inline.viza_xizmatlari_inline import ish_dav, sayohat_dav, oqish_dav

from loader import dp

import logging

logging.basicConfig(level=logging.INFO)


@dp.message_handler(text="Visa xizmatlari")
async def visa_xizmat(msg: types.Message):
    await msg.answer("Kerakli bo'limni tanlang:", reply_markup=visa_xizmatlari)


@dp.message_handler(text="Ish vizalari")
async def visa_xizmat(msg: types.Message):
    await msg.answer("Davlatni tanlang:", reply_markup=ish_dav)


@dp.message_handler(text="Sayohat vizalari")
async def visa_xizmat(msg: types.Message):
    await msg.answer("Davlatni tanlang:", reply_markup=sayohat_dav)


@dp.message_handler(text="O'qish vizalari")
async def visa_xizmat(msg: types.Message):
    await msg.answer("Davlatni tanlang:", reply_markup=oqish_dav)


@dp.message_handler(text="↩️ Ortga")
async def visa_xizmat(msg: types.Message):
    await msg.answer("↩️ Ortga", reply_markup=menu)


