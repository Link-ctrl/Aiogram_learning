from aiogram import Bot, Dispatcher, executor, types


TOKEN_API = "6231684827:AAEv_LHi7QGXSrJYGtX11g9F0h4lcrgP-CA"  # токен для подключения к телеграм API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.count(' ') >= 1:
        await message.answer(text = message.text) # написать сообщение text


if __name__ == '__main__':
    executor.start_polling(dp)