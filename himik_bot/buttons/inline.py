from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from himik_bot.buttons.text import *



def back_inline(lang='uz'):
    texts = {
        'uz': ortga,
        'ru': nazad,

    }

    back_text = texts.get(lang, texts['uz'])
    back_button = InlineKeyboardButton(text=back_text, callback_data='back')
    return InlineKeyboardMarkup(inline_keyboard=[[back_button]])


def answer_admin(user_id):
    keyboard1 = InlineKeyboardButton(text="Javob berish 📝", callback_data=f'answer_{user_id}')
    return InlineKeyboardMarkup(inline_keyboard=[[keyboard1]])
