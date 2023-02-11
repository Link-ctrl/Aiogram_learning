from aiogram import Bot, executor, Dispatcher, types

TOKEN_API = "6195302074:AAE7URz4s3O5_YKu_H99zK67aZanoH8J4bY"

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="бла бла бла")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text="Описание бота")

if __name__ == "__main__":
    executor.start_polling(dp)