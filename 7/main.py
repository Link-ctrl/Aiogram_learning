from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

from config import TOKEN_API


HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='bla bla bla',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text = HELP_COMMAND)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text = '❤️',
                               callback_data='like')
    ib2 = InlineKeyboardButton(text = '👎',
                               callback_data='Dislike')
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://memepedia.ru/wp-content/uploads/2018/12/kot-kashlyaet-mem.png',
                         caption='Do you like what you see?',
                         reply_markup=ikb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text = 'You like what you see')
    await callback.answer(text = "You don't like what you see")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)