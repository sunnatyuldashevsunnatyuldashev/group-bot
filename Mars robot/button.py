from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# bosh_menu_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Ota onalar", callback_data="Ota onalar"),
#             InlineKeyboardButton(text="O'quvchi", callback_data="O'quvchi"),
#             InlineKeyboardButton(text="Mehmon", callback_data="Mehmon"),
#         ]
#     ]
# )

# ota_ona_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Maktab haqida"),
#             KeyboardButton(text="Farzandni ro'yhatdan o'tkazish"),
#         ]
#     ],
#     resize_keyboard=True
# )



bosh_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="имя", callback_data="имя"),
            InlineKeyboardButton(text="фамиля", callback_data="фамиля"),
           
        ],
        [
             InlineKeyboardButton(text="город", callback_data="город"),
             InlineKeyboardButton(text="тел номер", callback_data="тел номер"),
         ],
         [
              InlineKeyboardButton(text="филиал", callback_data="филиал"),
              InlineKeyboardButton(text="Язык", callback_data="Язык"),
         ],
         
    ],
    
)



filial = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="yunusobod filiali"),
            KeyboardButton(text="Tinchlik filiali")
        ],
        [
            KeyboardButton(text="Chilonzor 1"),
            KeyboardButton(text="Chilonzor 2")
        ]
    ],
    resize_keyboard=True
)









about_school = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="работый учеников", callback_data="работый учеников"),
            InlineKeyboardButton(text="переподаватели", callback_data="переподаватели"),
           
        ],
        [
             InlineKeyboardButton(text="экскурсия по школе", callback_data="экскурсия по школе"),
             InlineKeyboardButton(text="отзыв", callback_data="отзыв"),
         ],
         [
             
              InlineKeyboardButton(text="философия школы", callback_data="философия школы"),
         ]
    ],
    
)


shop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mars notebook"),
            InlineKeyboardButton(text="Mars pen"),
        ],
        [
            InlineKeyboardButton(text="USB fleshka"),
            InlineKeyboardButton(text="Keyboard"),
        ],
        [
            InlineKeyboardButton(text="Mause"),
            InlineKeyboardButton(text="Mars chocolate"),
        ],
        [
            InlineKeyboardButton(text="Strobar"),
            InlineKeyboardButton(text="Mars mini"),
        ],
        [
            InlineKeyboardButton(text="Mars sticker"),
            InlineKeyboardButton(text="Mars rug"),
        ],
    ]
)










































from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton



bosh_menu = InlineKeyboardMarkup(
    Inline_keyboard=[
        [
            InlineKeyboardButton(text="Ota onalar",callback_data="Ota onalar"),
            InlineKeyboardButton(text="O'quvchi",callback_data="Ota onalar"),
            InlineKeyboardButton(text="Mehmon",callback_data="Ota onalar"),
        ]
    ]
)


# ota_ona = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="maktab hakdia"),
#             KeyboardButton(text="Farzandni ro'yhatdan otkazish"),
#         ]
#     ],
#     resize_keyboard=True
# )

# profil = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="имя"call_back_date=),
#             InlineKeyboardButton(text="Фамиля")
#         ],
#         [
#             InlineKeyboardButton(text="Язык"),
#             InlineKeyboardButton(text="Телефон")
#         ],
#         [
#             InlineKeyboardButton(text="город"),
            
#         ]
#     ],
#      resize_keyboard=True
# )





