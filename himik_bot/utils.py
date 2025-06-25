from aiogram import Bot
from aiogram.types import BotCommand


# Bot commands setting
async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="🚀 Start the bot"),
        BotCommand(command="language", description="📋 Choose your language"),
    ]
    await bot.set_my_commands(commands)
