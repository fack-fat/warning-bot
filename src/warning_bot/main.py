import logging
from config import BOT
from hendlers.hendler import DP
from src.warning_bot.sourse.mongo import watcher_new

async def main():
    await asyncio.gather(
        DP.start_polling(BOT),
        watcher_new()
    )

if __name__ == '__main__':
    logging.log(level=logging.INFO, msg="start app")
    import asyncio
    asyncio.run(main())


