import logging
from src.warning_bot.config import DP
from aiogram.filters import Command
from aiogram import types, F

dp = DP

@dp.message(Command("start"))
async def start(message: types.Message):
    user = message.from_user
    logging.log(level=logging.INFO, msg=f"Start bot user: {user.id}, name: {user.first_name}, nickname: @{user.username}")
    await message.answer(f"Привет, {user.first_name}")


