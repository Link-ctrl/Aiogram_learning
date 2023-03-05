from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/links')
kb.add(b1, b2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text = 'нажми на кнопку',
                           url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
ib2 = InlineKeyboardButton(text = 'кнопка',
                           url= 'https://www.youtube.com/watch?v=5_EHfHbzUCo&list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&index=11')

ikb.add(ib1, ib2)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                         text ='старт бота',
                         reply_markup=kb)

@dp.message_handler(commands=['links'])
async def links_command(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text = 'бла бла бла',
                           reply_markup=ikb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)