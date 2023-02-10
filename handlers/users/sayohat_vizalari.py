from aiogram import types
from data.sayohat_davlatlar_haqida import *
from loader import dp
from keyboards.inline.viza_xizmatlari_inline import *


@dp.callback_query_handler(text="say_cana")
async def bolariya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('cana_say'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(cana_say_visa[int(a[-1]) - 1], reply_markup=cana_say_mal_tan)

    if bool(cana_say_visa) == 0:
        await callback.message.answer(
            "Kanada davlatiga afsuski hali visalarimiz yo'q.\nQo'shimcha malumot uchun Murojaat uchun tugmasini bosing.")
        pass
    else:
        add_ish_inline_keyboard(len(cana_say_visa), cana_say_mal_tan, callback.data)
        await callback.message.answer(cana_say_visa[0], reply_markup=cana_say_mal_tan)
        xorvatiya_ish_visa()

@dp.callback_query_handler(text="say_brit")
async def bolariya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('brit_say'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(brit_say_visa[int(a[-1]) - 1], reply_markup=brit_say_mal_tan)

    if bool(brit_say_visa) == 0:
        await callback.message.answer(
            "Britaniya davlatiga afsuski hali visalarimiz yo'q.\nQo'shimcha malumot uchun Murojaat uchun tugmasini bosing.")
        pass
    else:
        add_ish_inline_keyboard(len(brit_say_visa), brit_say_mal_tan, callback.data)
        await callback.message.answer(brit_say_visa[0], reply_markup=brit_say_mal_tan)
        xorvatiya_ish_visa()

@dp.callback_query_handler(text="say_shen")
async def bolariya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('shen_say'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(shengen_say_visa[int(a[-1]) - 1], reply_markup=shen_say_mal_tan)

    if bool(shengen_say_visa) == 0:
        await callback.message.answer(
            "Shengen hududiga afsuski hali visalarimiz yo'q.\nQo'shimcha malumot uchun Murojaat uchun tugmasini bosing.")
        pass
    else:
        add_ish_inline_keyboard(len(shengen_say_visa), shen_say_mal_tan, callback.data)
        await callback.message.answer(shengen_say_visa[0], reply_markup=shen_say_mal_tan)
        xorvatiya_ish_visa()
