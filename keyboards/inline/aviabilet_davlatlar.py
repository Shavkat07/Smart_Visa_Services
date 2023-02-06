from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


avio_bilet_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Rossiya", callback_data="bilet_ru"),
            InlineKeyboardButton(text="Turkiya", callback_data="bilet_turk"),
            InlineKeyboardButton(text="Angliya", callback_data="bilet_ang")
        ],
        [
            InlineKeyboardButton(text="Dubay", callback_data="bilet_dub"),
            InlineKeyboardButton(text="AQSH", callback_data="bilet_use"),
            InlineKeyboardButton(text="Germaniya", callback_data="bilet_germ")
        ],
        [
            InlineKeyboardButton(text="Latviya", callback_data="bilet_lat")
        ]
    )
)