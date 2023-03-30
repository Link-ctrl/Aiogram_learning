from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("/start")
b2 = KeyboardButton("/help")
b3 = KeyboardButton("/description")
kb.add(b1, b2, b3)

kb_pics = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Рандом')
bp2 = KeyboardButton(text='Главное меню')
kb_pics.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='',
                           url= '')
ib2 = InlineKeyboardButton(text= '',
                           url = '')
ikb.add(ib1, ib2)