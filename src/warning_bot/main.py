import logging
from config import BOT
from hendlers.hendler import DP

async def main():
    await DP.start_polling(BOT)

if __name__ == '__main__':
    logging.log(level=logging.INFO, msg="start app")
    import asyncio
    asyncio.run(main())


