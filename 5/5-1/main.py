from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - описание бота 
"""

async def on_startup(_):
    print('Бот запущен')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/❤️')
kb.add(b1).add(b2).add(b3)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Бот запущен',
                           parse_mode='HTML',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML',
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text = 'Этот бот бла бла бла',
                           parse_mode='HTML',
                           reply_markup=kb)

@dp.message_handler(commands=['❤️'])
async def heart_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEH2_1j9kq9BmkpN4fA7r6zVDXPosv-ZAAC-g8AArxz8Ev5ju7492idci4E",
                           reply_markup=kb)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)