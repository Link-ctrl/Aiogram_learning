from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начало работы</em>
<b>/картинка</b> - <em>выдаёт картинку </em>
<b>/description</b> - <em>Описание бота </em>
"""

async def on_startup(_):
    print('Бот запущен')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/description')
b3 = KeyboardButton('/картинка')
kb.add(b1).add(b2).add(b3)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text = 'Бот запущен',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = HELP_COMMAND, parse_mode='HTML' """reply_markup=ReplyKeyboardRemove()""")
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text = 'Этот бот что-то делает', parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://www.murcat.ru/mem/db/admin/foto/1605805833.jpg")
    await message.delete()

''''@dp.message_handler()
async def echo(message):
    await message.answer(message.text)'''

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
