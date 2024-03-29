from aiogram import Bot, executor, Dispatcher, types

from config import TOKEN_API


HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text="бла бла бла")
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)