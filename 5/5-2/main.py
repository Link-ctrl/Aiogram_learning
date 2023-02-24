from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/orange - отправляет фото апельсина
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/orange')
kb.add(b1).add(b2)

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text = 'Старт бота',
                           parse_mode='HTML',
                           reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML',
                           reply_markup=kb)

@dp.message_handler(commands=['orange'])
async def orange_command(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://eksmo.ru/upload/iblock/2c4/1_min.jpg')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)