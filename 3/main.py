from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('<em>бла бла бла</em>', parse_mode="HTML")

@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHvYJj64AjLttslegVNs8owmxESfjUXwAC9RIAAgihmUiusnOtMYtgHS4E")

@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + '👍')

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
