from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from himik_bot.buttons.text import *

def menu( lang='uz'):
    texts = {
        'uz': "Profile 👤",
        'ru': "Профиль 👤",
    }


    text1 = texts[lang]
    btn1 = KeyboardButton(text=text1)

    layout = [[btn1]]
    return ReplyKeyboardMarkup(keyboard=layout, resize_keyboard=True)

def language_btn():
    keyboard1 = KeyboardButton(text=uz_text)
    keyboard2 = KeyboardButton(text=ru_text)
    design = [[keyboard1, keyboard2]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def back(lang='uz'):
    text = {'uz': ortga, 'ru': nazad}[lang]

    keyboard1 = KeyboardButton(text=text)
    design = [[keyboard1]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

