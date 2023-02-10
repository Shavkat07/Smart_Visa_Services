from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.ish_davlatlar_haqida import *

ish_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Bolgariya", callback_data="ish_bolg"),
            InlineKeyboardButton(text="Rossiya", callback_data="ish_ross"),
            InlineKeyboardButton(text="Germaniya", callback_data="ish_germ")

        ],
        [
            InlineKeyboardButton(text="Buyuk Britaniya", callback_data="ish_brit"),
            InlineKeyboardButton(text="Latviya", callback_data="ish_latv"),
            InlineKeyboardButton(text="Slovakiya", callback_data="ish_slov")
        ],
        [
            InlineKeyboardButton(text="Xorvatiya", callback_data="ish_xorv"),
            InlineKeyboardButton(text="Janubiy Koreya", callback_data="ish_kore"),
            InlineKeyboardButton(text="Polsha", callback_data="ish_pols")
        ],
        [
            InlineKeyboardButton(text="Ruminiya", callback_data="ish_rumi"),
            InlineKeyboardButton(text="Gretsiya", callback_data="ish_gret")
        ]
    )
)

oqish_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Buyuk Britaniya", callback_data="oqish_brit"),
            InlineKeyboardButton(text="AQSH", callback_data="oqish_aqsh"),
            InlineKeyboardButton(text="Germaniya", callback_data="oqish_germ")
        ],
        [
            InlineKeyboardButton(text="Latviya", callback_data="oqish_latv"),
            InlineKeyboardButton(text="Canada", callback_data="oqish_cana"),
            InlineKeyboardButton(text="Shengen hududi", callback_data="oqish_sheng")
        ],
    )
)

sayohat_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Shengen hududiga", callback_data="say_sheng"),
            InlineKeyboardButton(text="Kanada", callback_data="say_kana"),
            InlineKeyboardButton(text="Buyuk Britaniya", callback_data="say_brit")
        ],
    )
)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
shen_say_mal_tan = InlineKeyboardMarkup()
cana_say_mal_tan = InlineKeyboardMarkup()
brit_say_mal_tan = InlineKeyboardMarkup()
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
latv_oquv_mal_tan = InlineKeyboardMarkup()
germ_oquv_mal_tan = InlineKeyboardMarkup()
brit_oquv_mal_tan = InlineKeyboardMarkup()
cana_oquv_mal_tan = InlineKeyboardMarkup()
shen_oquv_mal_tan = InlineKeyboardMarkup()
aqsh_oquv_mal_tan = InlineKeyboardMarkup()
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
rum_malumot_tanlash = InlineKeyboardMarkup()
polsha_malumot_tanlash = InlineKeyboardMarkup()
korey_malumot_tanlash = InlineKeyboardMarkup()
brit_malumot_tanlash = InlineKeyboardMarkup()
xorv_malumot_tanlash = InlineKeyboardMarkup()
slov_malumot_tanlash = InlineKeyboardMarkup()
bolg_malumot_tanlash = InlineKeyboardMarkup()
ross_malumot_tanlash = InlineKeyboardMarkup()
latv_malumot_tanlash = InlineKeyboardMarkup()
germ_malumot_tanlash = InlineKeyboardMarkup()
gret_malumot_tanlash = InlineKeyboardMarkup()


def add_ish_inline_keyboard(len, name, data_name):
    a = data_name[-4:]
    if data_name.startswith("oqish"):
        if bool(name.inline_keyboard) == 0:
            for i in range(1, len + 1):
                name.insert(InlineKeyboardButton(f'{i}', callback_data=f"_{a}_oqish_{i}"))
        else:
            pass
    elif data_name.startswith("ish"):
        if bool(name.inline_keyboard) == 0:
            for i in range(1, len + 1):
                name.insert(InlineKeyboardButton(f'{i}', callback_data=f"{a}_{i}"))
        else:
            pass

    elif data_name.startswith("say"):
        if bool(name.inline_keyboard) == 0:
            for i in range(1, len + 1):
                name.insert(InlineKeyboardButton(f'{i}', callback_data=f"{a}_say_{i}"))
        else:
            pass
