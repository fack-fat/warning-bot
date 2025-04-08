import logging
from src.warning_bot.config import DP, BOT
from aiogram.filters import Command
from aiogram import types, F

@DP.message(Command("start"))
async def start(message: types.Message):
    user = message.from_user
    logging.log(level=logging.INFO, msg=f"Start bot user: {user.id}, name: {user.first_name}, nickname: @{user.username}")
    await message.answer(f"Привет, {user.first_name}")


async def send_notification(message_data):
    try:
        text = f"{message_data['message']}"
        #TODO 100 заглушка, добавить айди чата
        await BOT.send_message(100, text)
    except Exception as e:
        logging.log(level=logging.WARN, msg=f"Error send message, data: {message_data['message']}, error: {e}")

