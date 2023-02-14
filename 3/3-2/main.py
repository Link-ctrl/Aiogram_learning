from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6195302074:AAE7URz4s3O5_YKu_H99zK67aZanoH8J4bY"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/give</b> - <em>выдаёт Дорна</em>
<b>/❤</b> - <em>выдаёт чёрное сердечко </em>
"""

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await message.reply('Ля, какой Дорн ' + '❤️')
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHvYJj64AjLttslegVNs8owmxESfjUXwAC9RIAAgihmUiusnOtMYtgHS4E")

@dp.message_handler(commands=['❤️'])
async def send_emoji(message: types.Message):
    await message.reply('🖤')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text = message.text.count('✅'))

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
