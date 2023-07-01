


import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


API_TOKEN = '6237263265:AAH9CxBX9sCcQgCEzdmR1Fh3HOH1JDG8F5I'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello", reply_markup=menu)


menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="savollar❓"),
            KeyboardButton(text="videolar🎞"),
            KeyboardButton(text="audio🎶")
        ],
        [
            KeyboardButton(text="Gif 🎁"),
            KeyboardButton(text="Voice"),
            KeyboardButton(text="photo🖼")
        ],
        [
            KeyboardButton(text="Contact"),
            KeyboardButton(text="location📍"),
            KeyboardButton(text="stiker😁")
        ]
    ],
    resize_keyboard=True
)


savolar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 answer"),
            KeyboardButton(text="2 answer"),
            KeyboardButton(text="3 answer")
        ],
        [
            KeyboardButton(text="exit")
        ],
        
    ],
    resize_keyboard=True
)
@dp.message_handler(text="savollar❓")
async def echo(message: types.Message):
    await message.answer("najmite knpku", reply_markup=savolar)


@dp.message_handler(text="1 answer")
async def echo(message: types.Message):
    await message.answer_poll(options="https://t.me/tannus8002/25")

@dp.message_handler(text="2 answer")
async def echo(message: types.Message):
    await message.answer_poll("https://t.me/tannus8002/27")

@dp.message_handler(text="3 answer")
async def echo(message: types.Message):
    await message.answer_poll("https://t.me/tannus8002/25")







video_velu = ReplyKeyboardMarkup(
   keyboard= [
        [
          KeyboardButton(text="1 video🎞"),
          KeyboardButton(text="2 video🎞"),
          KeyboardButton(text="3 video🎞")
        ],
        [
        KeyboardButton(text="exit")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="videolar🎞")
async def echo(message: types.Message):
    await message.answer("choose one button", reply_markup=video_velu)

@dp.message_handler(text="1 video🎞")
async def echo(message: types.Message):
    await message.answer_video("https://t.me/Prikollar_Kulguli_Hazillar/1429")

@dp.message_handler(text="2 video🎞")
async def echo(message: types.Message):
    await message.answer_video("https://t.me/Prikollar_Kulguli_Hazillar/1428")

@dp.message_handler(text="3 video🎞")
async def echo(message: types.Message):
    await message.answer_video("https://t.me/Prikollar_Kulguli_Hazillar/1424")





audio = ReplyKeyboardMarkup(
   keyboard= [
        [
          KeyboardButton(text=" 1 audio"),
          KeyboardButton(text="2 audio"),
          KeyboardButton(text="3 audio")
        ],
        [
        KeyboardButton(text="exit")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="audio🎶")
async def echo(message: types.Message):
    await message.answer("choose one button", reply_markup=audio)


@dp.message_handler(text="1 audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/tannus8002/4")

@dp.message_handler(text="2 audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/tannus8002/5")

@dp.message_handler(text="3 audio")
async def echo(message: types.Message):
    await message.answer_audio("https://t.me/tannus8002/6")






gif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 gif"),
            KeyboardButton(text="2 gif"),
            KeyboardButton(text="3 gif")
        ],
        [
            KeyboardButton(text="exit")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Gif 🎁")
async def echo(message: types.Message):
    await message.answer("choose one button", reply_markup=gif)


@dp.message_handler(text="1 gif")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/groupback447/2")

@dp.message_handler(text="2 gif")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/groupback447/3")

@dp.message_handler(text="3 gif")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/groupback447/2")










@dp.message_handler(text="1 audio")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/tannus8002/7")

@dp.message_handler(text="2 audio")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/tannus8002/8")

@dp.message_handler(text="3 audio")
async def echo(message: types.Message):
    await message.answer_animation("hhttps://t.me/tannus8002/9")



photo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 photo"),
            KeyboardButton(text="2 photo"),
            KeyboardButton(text="3 photo")
        ],
        [
          KeyboardButton(text="exit")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="photo🖼")
async def echo(message: types.Message):
    await message.answer("choose one button", reply_markup=photo)


@dp.message_handler(text="1 photo")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/tannus8002/16")


@dp.message_handler(text="2 photo")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/tannus8002/17")


@dp.message_handler(text="3 photo")
async def echo(message: types.Message):
    await message.answer_photo("https://t.me/tannus8002/18")


voice = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton("Voice 1"),
        KeyboardButton("Voice 2"),
        KeyboardButton("Voice 3")
        ],
        [
            KeyboardButton("exit")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Voice")
async def echo(message: types.Message):
    await message.answer("najmite knpku", reply_markup=voice)

@dp.message_handler(text="Voice 1")
async def echo(message: types.Message):
    await message.answer_voice("https://t.me/tannus8002/13")


@dp.message_handler(text="Voice 2")
async def echo(message: types.Message):
    await message.answer_voice("https://t.me/tannus8002/14")


@dp.message_handler(text="Voice 3")
async def echo(message: types.Message):
    await message.answer_voice("https://t.me/tannus8002/15")


contacts = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 contact"),
            KeyboardButton(text="2 contact"),
            KeyboardButton(text="3 contact")
        ],
        [
            KeyboardButton(text="exit")
        ],
        
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Contact")
async def echo(message: types.Message):
    await message.answer("my family's contact's", reply_markup=contacts)


@dp.message_handler(text="1 contact")
async def echo(message: types.Message):
    await message.answer_contact(phone_number="+998947033630", first_name="Sunnat")

@dp.message_handler(text="2 contact")
async def echo(message: types.Message):
    await message.answer_contact(phone_number="+998990419141", first_name="MOM")

@dp.message_handler(text="3 contact")
async def echo(message: types.Message):
    await message.answer_contact(phone_number="+998935363630",first_name="Father")






location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 location ctroy centre"),
            KeyboardButton(text="2 location my hause"),
            KeyboardButton(text="3 location my school")
        ],
        [
            KeyboardButton(text="exit")
        ],
        
    ],
    resize_keyboard=True
)
@dp.message_handler(text="location📍")
async def echo(message: types.Message):
    await message.answer("choose location", reply_markup=location)


@dp.message_handler(text="1 location ctroy centre")
async def echo(message: types.Message):
    await message.answer_location(41.36535809665692, 69.28837394096497)

@dp.message_handler(text="2 location my hause")
async def echo(message: types.Message):
    await message.answer_location(41.39703709309513, 69.34730047010336)

@dp.message_handler(text="3 location     my school")
async def echo(message: types.Message):
    await message.answer_location(40.916033182084405, 69.01558190252565)








sticker = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 sticker"),
            KeyboardButton(text="2 sticker"),
            KeyboardButton(text="3 sticker")
        ],
        [
            KeyboardButton(text="exit")
        ],
        
    ],
    resize_keyboard=True
)
@dp.message_handler(text="stiker😁")
async def echo(message: types.Message):
    await message.answer("choose button", reply_markup=sticker)


@dp.message_handler(text="1 sticker")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/tannus8002/28")

@dp.message_handler(text="2 sticker")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/tannus8002/29")

@dp.message_handler(text="3 sticker")
async def echo(message: types.Message):
    await message.answer_animation("https://t.me/tannus8002/30")








@dp.message_handler(text="exit")
async def echo(message: types.Message):
    await message.answer("you are exit", reply_markup=menu)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)