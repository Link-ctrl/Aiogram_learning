"""
Постановка задачи:
1.  Бот должен быть реализован таким образом,
    чтобы все обновления пропускались при оффлайн режиме.

    При включении сервера в консоли должна отображаться информация по данному поводу.
    DONE

2.  Бот должен быть реализован в двух файлах.
    В первом файле - клавиатура пользователя.
    Во втором - файл main.py, где расположен остальной функционал бота.
    DONE

3.  У бота должны быть реализованы команды /start, /help, /description
    Должно присутствовать главное меню с клавиатурой,
    где пользователь может использовать каждую из этих команд.
    DONE

4.  Должно быть реализовано меню,
    где пользователь может получить одну рандомную фотографию из заранее определённого списка.
    Оттуда должен быть переход на главное меню.
    DONE

5.  Под фотографией должно быть описание данной фотографии.
    При этом должна также присутствовать инлайн клавиатура.

    При нажатии должен генерироваться callback запрос, ему
    должна быть сопоставлена обработка со стороны сервера.

6.  Инлайн клавиатура будет состоять из трёх кнопок:
    - Следующая рандомная фотография
    - Лайк
    - Дизлайк
    Если пользователь нажмёт на лайк/дислайк,
    должен появиться соответствующий label. Обработайте
    как-либо повторное нажатие на кнопку при одном и той же фото.

7.  Реализуйте у бота возможность отправлять вам стикеры,
    эмодзи и рандомное местоположение.
"""
from random import choice

from aiogram import Bot, executor, Dispatcher, types

from config import TOKEN_API

from keyboard import kb, kb2, ikb

HELP_COMMAND = """
/start - начать работу с ботом
/help - список команд
/description - описание бота
/pics - присылает рандомное фото из списка
"""
pics = ('https://avatars.dzeninfra.ru/get-zen_doc/1671806/pub_5e0e064fddfef600b0937786_5e0e067bdf944400b120fa1a/scale_1200',
        'https://cdn.ren.tv/cache/960x540/media/img/a5/e7/a5e7b0666dcfb9a7698c62fde870ff57bba698ea.jpg',
        'https://memepedia.ru/wp-content/uploads/2019/10/chipseki-mem.png')

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='СТАРТ БОТА',
                           reply_markup=kb)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='бот делает что-то',
                           reply_markup=kb)

@dp.message_handler(commands=['pics'])
async def random_pics(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=choice(pics),
                         reply_markup=kb2)

@dp.message_handler(commands=['back'])
async def back_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='возврат',
                           reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)