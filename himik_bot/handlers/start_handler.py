from aiogram import F
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from django.conf import settings

from himik_bot.dispatcher import dp
from himik_bot.buttons.reply import language_btn
from himik_bot.buttons.text import *
from himik_bot.state.LanguageState import LanguageState
from himik_bot.models import User


@dp.message(Command("language"), StateFilter(None))
async def language(message: Message, state: FSMContext) -> None:
    await state.set_state(LanguageState.language)
    await select_language_message(message, state)
    return


@dp.message(Command("start"), StateFilter(None))
async def start(message: Message, state: FSMContext) -> None:
    tg_id = message.from_user.id
    await state.update_data(tg_id=tg_id)
    user, created = User.objects.get_or_create(tg_id=tg_id)
    if user.lang:
        await state.update_data(lang=user.lang)
        await menu_handler(message, state)
        return

    if user.lang:
        await state.update_data(lang=user.lang)
        await menu_handler(message, state)
        return

    await message.answer(
        text=all.get("lang_choice"),
        reply_markup=language_btn()
    )
    await state.set_state(LanguageState.language)
    return


@dp.message(StateFilter(LanguageState.language))
async def select_language_message(message: Message, state: FSMContext) -> None:
    tg_id = message.from_user.id
    await state.update_data(tg_id=tg_id)
    if message.text == uz_text:
        User.objects.update_or_create(
            tg_id=tg_id, defaults={'lang': 'uz'}
        )
        await state.update_data(lang='uz')
    elif message.text == ru_text:
        User.objects.update_or_create(
            tg_id=tg_id, defaults={'lang': 'ru'}
        )
        await state.update_data(lang='ru')
    else:
        await message.answer(
            text=all.get("lang_choice"),
            reply_markup=language_btn()
        )
        return
    await menu_handler(message, state)
    return


async def menu_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    lang = data.get('lang')
    tg_id = data.get('tg_id')
    if not lang:
        user = User.objects.filter(tg_id=tg_id).first()
        lang = user.lang if user else 'uz'
        await state.update_data(lang=lang)
    if lang == 'uz':
        await message.answer(text=uz.get('greating'),reply_markup=ReplyKeyboardRemove())
        await message.answer_video(video=settings.VIDEO_ID, caption=uz.get('menu_text'),
                                   reply_markup=ReplyKeyboardRemove()
                                   )
    else:
        await message.answer(text=ru.get('greating'), reply_markup=ReplyKeyboardRemove())
        await message.answer_video(video=settings.VIDEO_ID, caption=ru.get('menu_text'), reply_markup=ReplyKeyboardRemove()
                                   )
    await state.set_state(None)


@dp.message(StateFilter(None), lambda message: message.text in (nazad, ortga))
async def to_back(message: Message, state: FSMContext) -> None:
    tg_id = message.from_user.id
    await state.update_data(tg_id=tg_id)
    await message.delete()
    await menu_handler(message, state)
    return


@dp.callback_query(StateFilter(None), F.data == "back")
async def back_to_menu(callback_query: CallbackQuery, state: FSMContext) -> None:
    await callback_query.answer()
    await callback_query.message.delete()
    await menu_handler(callback_query.message, state)
    return
