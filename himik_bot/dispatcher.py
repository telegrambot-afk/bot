from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from django.conf import settings

dp = Dispatcher(storage=MemoryStorage())
TOKEN=settings.TOKEN
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
