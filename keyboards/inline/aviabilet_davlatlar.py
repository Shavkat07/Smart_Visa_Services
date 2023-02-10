from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


avio_bilet_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Rossiya", callback_data="bilet_ross"),
            InlineKeyboardButton(text="Turkiya", callback_data="bilet_turk"),
            InlineKeyboardButton(text="Angliya", callback_data="bilet_angl")
        ],
        [
            InlineKeyboardButton(text="Dubay", callback_data="bilet_duba"),
            InlineKeyboardButton(text="AQSH", callback_data="bilet_aqsh"),
            InlineKeyboardButton(text="Germaniya", callback_data="bilet_germ")
        ],
        [
            InlineKeyboardButton(text="Latviya", callback_data="bilet_latv")
        ]
    )
)


def aviabilet_inline(len, name, data_name):
    a = data_name[-4:]
    if data_name.startswith("say"):
        if bool(name.inline_keyboard) == 0:
            for i in range(1, len + 1):
                name.insert(InlineKeyboardButton(f'{i}', callback_data=f"{a}_avia_{i}"))
        else:
            pass

