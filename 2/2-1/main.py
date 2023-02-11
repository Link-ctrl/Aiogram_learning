from aiogram import Bot, executor, Dispatcher, types
from random import choice

TOKEN_API = "6195302074:AAE7URz4s3O5_YKu_H99zK67aZanoH8J4bY"


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="бла бла бла")
    await message.delete()

@dp.message_handler(commands=['random'])
async def random_command(message: types.Message):
    await message.answer(text=choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

if __name__ == "__main__":
    executor.start_polling(dp)