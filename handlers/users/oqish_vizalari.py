from aiogram import types
from data.oqish_davlat_haqida import *
from loader import dp
from keyboards.inline.viza_xizmatlari_inline import *


@dp.callback_query_handler(text="oqish_germ")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_germ'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(germ_oqish_visa[int(a[-1]) - 1], reply_markup=germ_oquv_mal_tan)

    add_ish_inline_keyboard(len(germ_oqish_visa), germ_oquv_mal_tan, callback.data)
    await callback.message.answer(germ_oqish_visa[0], reply_markup=germ_oquv_mal_tan)
    bolgariya_ish_visa()


@dp.callback_query_handler(text="oqish_brit")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_brit'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(brit_oqish_visa[int(a[-1]) - 1], reply_markup=brit_oquv_mal_tan)

    add_ish_inline_keyboard(len(brit_oqish_visa), brit_oquv_mal_tan, callback.data)
    await callback.message.answer(brit_oqish_visa[0], reply_markup=brit_oquv_mal_tan)
    bolgariya_ish_visa()



@dp.callback_query_handler(text="oqish_latv")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_latv'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(latv_oqish_visa[int(a[-1]) - 1], reply_markup=latv_oquv_mal_tan)

    add_ish_inline_keyboard(len(latv_oqish_visa), latv_oquv_mal_tan, callback.data)
    await callback.message.answer(latv_oqish_visa[0], reply_markup=latv_oquv_mal_tan)
    bolgariya_ish_visa()


@dp.callback_query_handler(text="oqish_aqsh")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_aqsh'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(aqsh_oqish_visa[int(a[-1]) - 1], reply_markup=aqsh_oquv_mal_tan)

    add_ish_inline_keyboard(len(aqsh_oqish_visa), aqsh_oquv_mal_tan, callback.data)
    await callback.message.answer(aqsh_oqish_visa[0], reply_markup=aqsh_oquv_mal_tan)
    bolgariya_ish_visa()


@dp.callback_query_handler(text="oqish_cana")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_cana'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(cana_oqish_visa[int(a[-1]) - 1], reply_markup=cana_oquv_mal_tan)

    if bool(cana_oqish_visa) == 0:
        pass
    else:
        add_ish_inline_keyboard(len(cana_oqish_visa), cana_oquv_mal_tan, callback.data)
        await callback.message.answer(cana_oqish_visa[0], reply_markup=cana_oquv_mal_tan)
        bolgariya_ish_visa()


@dp.callback_query_handler(text="oqish_shen")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('_shen'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(shen_oqish_visa[int(a[-1]) - 1], reply_markup=shen_oquv_mal_tan)

    if bool(cana_oqish_visa) == 0:
        pass
    else:
        add_ish_inline_keyboard(len(shen_oqish_visa), shen_oquv_mal_tan, callback.data)
        await callback.message.answer(shen_oqish_visa[0], reply_markup=shen_oquv_mal_tan)
        bolgariya_ish_visa()
