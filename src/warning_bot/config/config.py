import os
import logging
import sys

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

file_handler = logging.FileHandler("log-info.log", encoding="utf-8")
console_handler = logging.StreamHandler(sys.stdout)

load_dotenv()
logging.basicConfig(
    format="%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
    handlers=[file_handler, console_handler]
)

TOKEN = os.getenv("TOKEN")

if len(TOKEN) > 0:
    BOT = Bot(TOKEN)
    DP = Dispatcher()
else:
    raise Exception("Bot token is empty")