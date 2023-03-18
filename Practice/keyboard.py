from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("/start")
b2 = KeyboardButton("/help")
b3 = KeyboardButton("/description")
b4 = KeyboardButton('/pics')
kb.add(b1, b2, b3, b4)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b_back = KeyboardButton("/back")
kb2.add(b_back)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='',
                           url= '')
ib2 = InlineKeyboardButton(text= '',
                           url = '')
ikb.add(ib1, ib2)