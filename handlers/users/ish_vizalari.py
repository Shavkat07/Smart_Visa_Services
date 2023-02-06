from aiogram import types
from data.ish_davlatlar_haqida import *
from loader import dp
from keyboards.inline.viza_xizmatlari_inline import *


########################################################################################


@dp.callback_query_handler(text="ish_ross")
async def bolariya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('ross'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(ross_ish_visa[int(a[-1]) - 1], reply_markup=ross_malumot_tanlash)

    add_ish_inline_keyboard(len(ross_ish_visa), ross_malumot_tanlash, callback.data)
    await callback.message.answer(ross_ish_visa[0], reply_markup=ross_malumot_tanlash)
    xorvatiya_ish_visa()


#########################################################################################################


@dp.callback_query_handler(text="ish_germ")
async def bolariya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('germ'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(german_ish_visa[int(a[-1]) - 1], reply_markup=germ_malumot_tanlash)

    add_ish_inline_keyboard(len(german_ish_visa), germ_malumot_tanlash, callback.data)
    await callback.message.answer(german_ish_visa[0], reply_markup=germ_malumot_tanlash)
    xorvatiya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_latv")
async def bolariya_bilet(callback: types.CallbackQuery):
    def latviya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('latv'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(latv_ish_visa[int(a[-1]) - 1], reply_markup=latv_malumot_tanlash)

    add_ish_inline_keyboard(len(latv_ish_visa), latv_malumot_tanlash, callback.data)
    await callback.message.answer(latv_ish_visa[0], reply_markup=latv_malumot_tanlash)
    latviya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_slov")
async def bolariya_bilet(callback: types.CallbackQuery):
    def slovakiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('slov'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(slov_ish_visa[int(a[-1]) - 1], reply_markup=slov_malumot_tanlash)

    add_ish_inline_keyboard(len(slov_ish_visa), slov_malumot_tanlash, callback.data)
    await callback.message.answer(slov_ish_visa[0], reply_markup=slov_malumot_tanlash)
    slovakiya_ish_visa()


#########################################################################################################


@dp.callback_query_handler(text="ish_xorv")
async def xorvatiya_bilet(callback: types.CallbackQuery):
    def xorvatiya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('xorv'))
        async def xorv_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(xorvat_ish_visa[int(a[-1]) - 1], reply_markup=xorv_malumot_tanlash)

    add_ish_inline_keyboard(len(xorvat_ish_visa), xorv_malumot_tanlash, callback.data)
    await callback.message.answer(xorvat_ish_visa[0], reply_markup=xorv_malumot_tanlash)
    xorvatiya_ish_visa()


#########################################################################################################


@dp.callback_query_handler(text="ish_bolg")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('bolg'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(bolg_ish_visa[int(a[-1]) - 1], reply_markup=bolg_malumot_tanlash)

    add_ish_inline_keyboard(len(bolg_ish_visa), bolg_malumot_tanlash, callback.data)
    await callback.message.answer(bolg_ish_visa[0], reply_markup=bolg_malumot_tanlash)
    bolgariya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_pols")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('pols'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(polsha_ish_visa[int(a[-1]) - 1], reply_markup=polsha_malumot_tanlash)

    add_ish_inline_keyboard(len(polsha_ish_visa), polsha_malumot_tanlash, callback.data)
    await callback.message.answer(polsha_ish_visa[0], reply_markup=polsha_malumot_tanlash)
    bolgariya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_kore")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('kore'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(korey_ish_visa[int(a[-1]) - 1], reply_markup=korey_malumot_tanlash)

    add_ish_inline_keyboard(len(korey_ish_visa), korey_malumot_tanlash, callback.data)
    await callback.message.answer(korey_ish_visa[0], reply_markup=korey_malumot_tanlash)
    bolgariya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_rumi")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('rumi'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(rum_ish_visa[int(a[-1]) - 1], reply_markup=rum_malumot_tanlash)

    add_ish_inline_keyboard(len(rum_ish_visa), rum_malumot_tanlash, callback.data)
    await callback.message.answer(rum_ish_visa[0], reply_markup=rum_malumot_tanlash)
    bolgariya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_brit")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('brit'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(brit_ish_visa[int(a[-1]) - 1], reply_markup=brit_malumot_tanlash)

    add_ish_inline_keyboard(len(brit_ish_visa), brit_malumot_tanlash, callback.data)
    await callback.message.answer(brit_ish_visa[0], reply_markup=brit_malumot_tanlash)
    bolgariya_ish_visa()


#########################################################################################################

@dp.callback_query_handler(text="ish_gret")
async def bolariya_bilet(callback: types.CallbackQuery):
    def bolgariya_ish_visa():
        @dp.callback_query_handler(lambda c: c.data.startswith('gret'))
        async def bolg_bilet(callback: types.CallbackQuery):
            a = callback.data
            await callback.message.delete()
            await callback.message.answer(gret_ish_visa[int(a[-1]) - 1], reply_markup=gret_malumot_tanlash)

    add_ish_inline_keyboard(len(gret_ish_visa), gret_malumot_tanlash, callback.data)
    await callback.message.answer(gret_ish_visa[0], reply_markup=gret_malumot_tanlash)
    bolgariya_ish_visa()
