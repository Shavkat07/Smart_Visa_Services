from aiogram import types
from keyboards.inline import aviabilet_davlatlar
from data.aviabiletlar_haqida import *
from keyboards.inline.aviabilet_davlatlar import aviabilet_inline
from loader import dp

import logging

logging.basicConfig(level=logging.INFO)


@dp.message_handler(text="Aviabiletlar")
async def visa_xizmat(msg: types.Message):
    await msg.answer("Davlatni tanlang:", reply_markup=aviabilet_davlatlar.avio_bilet_dav)


@dp.message_handler(text="Murojat uchun:")
async def murojat_uchun(msg: types.Message):
    await msg.answer("""Batafsil ma’lumot olish uchun:

09-00 dan 18-00 gacha

📲+998999300037 | Samarqand

📲+998882237788 | Samarqand""")


@dp.message_handler(text="Kerakli xujjatlar")
async def kerakli_hujjatlar(msg: types.Message):
    await msg.answer("""📂Hujjatlar:
1. Zagran passport va yashil passport
2. Anketa  (o'zimiz to'ldiramiz)
3. Elektron rasm 3.5x4.5
4. Tugilganlik haqida guvohnoma
5. Nikoh guvohnomasi
6. Haydovchilik guvohnomasi (agar bor bo'lsa)
8. Sudlanmaganlik spravkasi (rus tilida, pechati bilan bo'lishi kerak)
9. Oila a'zolar pasport yoki metrikasi (ota ona, turmush ortoq, farzandlar)

❗️Hamma hujjatlarni kompyuterxonadan scaner qilib yuboring iltimos.

▫️ Viza olish muddati o'rtacha 2-3 oy.""")


# @dp.callback_query_handler(text="bilet_ross")
# async def bolariya_bilet(callback: types.CallbackQuery):
#     def xorvatiya_ish_visa():
#         @dp.callback_query_handler(lambda c: c.data.startswith('bilet'))
#         async def xorv_bilet(callback: types.CallbackQuery):
#             a = callback.data
#             await callback.message.delete()
#             await callback.message.answer(ross_aviabilet[int(a[-1]) - 1], reply_markup=ross_malumot_tanlash)
#
#     aviabilet_inline(len(ross_aviabilet), ross_malumot_tanlash, callback.data)
#     await callback.message.answer(ross_aviabilet[0], reply_markup=ross_malumot_tanlash)
#     xorvatiya_ish_visa()

