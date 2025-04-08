import os
import logging
import sys

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from motor.motor_asyncio import AsyncIOMotorClient


# .env init
load_dotenv()

TOKEN = os.getenv("TOKEN")
MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

#init logger
file_handler = logging.FileHandler("log-info.log", encoding="utf-8")
console_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    format="%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
    handlers=[file_handler, console_handler]
)

#init bot
if len(TOKEN) > 0:
    BOT = Bot(TOKEN)
    DP = Dispatcher()
else:
    raise Exception("Bot token is empty")

#init mongo
client = AsyncIOMotorClient(MONGO_URL)
db = client[f"{DATABASE_NAME}"]
COLLECTION = db[f"{COLLECTION_NAME}"]


