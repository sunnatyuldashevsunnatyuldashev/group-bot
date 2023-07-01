import logging

from aiogram import Bot, Dispatcher, executor, types
from button import *

API_TOKEN = '6237263265:AAH9CxBX9sCcQgCEzdmR1Fh3HOH1JDG8F5I'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variantni tanlang", 
                         reply_markup=menu)



menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑‍🎓 Профиль"),
            KeyboardButton(text="🪙 Мои монеты"),
            KeyboardButton(text="Space Shop💥")
        ],
        [
            KeyboardButton(text="🏫О школе"),
            KeyboardButton(text="✍️Оставить отзыв")
        ]
    ],
    resize_keyboard=True
)




@dp.message_handler(text="🧑‍🎓 Профиль")
async def send_welcome(message: types.Message):
    await message.answer("""  🧑‍🎓 Профиль
Имя: Sunnatjon
Фамилия: Yuldashev
Язык: ru
Телефон: 990419141
Город: tashkent
Учебный центр: YUNUSABAD""", 
                         reply_markup=bosh_menu_keyboard)



@dp.callback_query_handler(text="имя")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Assalomu alaykum hurmatli ota-ona!", reply_markup=menu)


@dp.callback_query_handler(text="фамиля")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Assalomu alaykum hurmatli mehmon!")


@dp.callback_query_handler(text="город")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Assalomu alaykum dangasa o'quvchi!")








@dp.message_handler(text="🪙 Мои монеты")
async def send_welcome(message: types.Message):
    await message.reply("ваши марс coin: 10")






@dp.message_handler(text="✍️Оставить отзыв")
async def send_welcome(message: types.Message):
    # await message.reply("напишите свое отзыв")
    await message.answer_photo("https://t.me/tannus8002/42",
                               caption="напишите свое отзыв")

@dp.callback_query_handler(text="филиал")
async def echo(call: types.CallbackQuery):
    await call.message.answer("филиалы танланг")














@dp.message_handler(text="Space Shop💥")
async def send_welcome(message: types.Message):
    await message.reply("выберите приз", reply_markup=shop)
    # await call.message.answer_photo("https://t.me/tannus8002/43")
    # async def echo(call: types.CallbackQuery):


    #  await call.message.answer_photo("https://t.me/tannus8002/44")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/45")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/46")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/47")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/48")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/49")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/50")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/51")
    # async def echo(call: types.CallbackQuery):
    #  await call.message.answer_photo("https://t.me/tannus8002/52")
    # async def echo(call: types.CallbackQuery):

     



@dp.message_handler()
async def send_welcome(message: types.Message):
    #  await message.delete ()
     await message.reply("спасибо за отзыв ваши отзыв пренимается мы так просто не ост авим", reply_markup=menu)
     
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)














































































































# import logging

# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from button import *
# API_TOKEN = '6237263265:AAH9CxBX9sCcQgCEzdmR1Fh3HOH1JDG8F5I'

# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)

# menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="🧑‍🎓 Профиль"),
#             KeyboardButton(text="🪙 Мои монеты"),
#             KeyboardButton(text="Space Shop💥")
#         ],
#         [
#             KeyboardButton(text="🏫О школе"),
#             KeyboardButton(text="✍️Оставить отзыв")
#         ]
#     ],
#     resize_keyboard=True
# )



# coin =  ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text="Мои марс монеты: 1")
#         ]
#     ],
#     resize_keyboard=True
# )

# @dp.message_handler(text="🪙 Мои монеты")
# async def echo(message: types.Message):
#     await message.reply("ваше коин в марсе",reply_markup=coin)




# # profil =  ReplyKeyboardMarkup(
# #     keyboard=[
# #         [
# #             KeyboardButton(text="Имя: Sunnat /n Фамиля: Yuldashev", )
# #         ]
        
# #     ],
# #     resize_keyboard=True
# # )



# @dp.message_handler(text="Space Shop💥")
# async def echo(message: types.Message):
#     await message.answer_photo("")




# @dp.callback_query_handler(text="🧑‍🎓 Профиль" )
# async def echo(call: types.CallbackQuery):
#     await call.message.answer("Ваше профиль",reply_markup=profil)








# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.reply("Hello" ,reply_markup=menu)



# @dp.message_handler(text="🏫О школе")
# async def send_welcome(message: types.Message):
#     await message.reply("Hello" ,reply_markup=bosh_menu)





# @dp.callback_query_handler(text="Ota onalar")
# async def send_welcome(message: types.Message):
#     await message.reply("Hello" ,reply_markup=ota_ona)






# @dp.callback_query_handler(text="Ota onalar", )
# async def echo(call: types.CallbackQuery):
#     await call.message.answer("Assalomu alaykum hurmatli ota onalar")
#     await call.answer("Valaykum alaykum hurmatli ota onalar")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)