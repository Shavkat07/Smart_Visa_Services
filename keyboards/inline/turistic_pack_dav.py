from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

tur_dav = InlineKeyboardMarkup(
    inline_keyboard=(
        [
            InlineKeyboardButton(text="Istanbul", callback_data="tur_ist"),
            InlineKeyboardButton(text="Antaliya", callback_data="tur_ant"),
            InlineKeyboardButton(text="Dubay", callback_data="tur_dub")
        ],
        [
            InlineKeyboardButton(text="Abu-Dabi", callback_data="tur_abu"),
            InlineKeyboardButton(text="Sharm-El-Shayx", callback_data="tur_sharm"),
            InlineKeyboardButton(text="Tayland", callback_data="tur_tay")

        ],
        [
            InlineKeyboardButton(text="Maldiv", callback_data="tur_mal"),
            InlineKeyboardButton(text="Rossiya", callback_data="tur_ross")
        ],
    )
)
