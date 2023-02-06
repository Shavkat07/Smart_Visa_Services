from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Visa xizmatlari"),
            KeyboardButton(text="Aviabiletlar"),
            KeyboardButton(text="Turistik paketlar")
        ],
        [
            KeyboardButton(text="Kerakli xujjatlar"),
            KeyboardButton(text="Murojat uchun:")
        ],
    ],
    resize_keyboard=True
)

visa_xizmatlari = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ish vizalari"),
            KeyboardButton(text="O'qish vizalari")

        ],
        [
            KeyboardButton(text="Sayohat vizalari"),
            KeyboardButton(text="↩️ Ortga")
        ]

    ],
    resize_keyboard=True
)



# menu = Visa xizmatlari(Ish vizalari(Angliya, Rossiya, Germaniya, Janubiy Koreya, Latviya, Slovakiya, Xorvatiya, Bolgariya), sayohat vizalari(Shengen hududiga), Oqish vizalari(Amerika, Canada, Angliya va Shengen hududi))  ,
# Aviabiletlar(Rossiya, Turkiya, Angliya, Dubay, AQSH, Germaniya, Latviya va boshqalar.),
# Turistik paketlar(Istanbul, Antaliya, Dubay, Abu-Dabi, Sharm-El-Shayx, Tayland, Maldiv, Rossiya),
# Kerakli xujjatlar(),
# Murojaat uchun(),
