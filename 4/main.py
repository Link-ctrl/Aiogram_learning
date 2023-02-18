from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начало работы</em>
<b>/картинка</b> - <em>выдаёт картинку </em>
"""

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['картинка'])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://www.murcat.ru/mem/db/admin/foto/1605805833.jpg")

@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id, latitude=55, longitude=74)
    await message.delete()


@dp.message_handler()
async def echo(message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
