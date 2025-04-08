import logging

from src.warning_bot.config import config
from src.warning_bot.hendlers import hendler

async def watcher_new():
    pipline = [{
        "$match": {
            "operationType": "insert",
            "fullDocument.is_read": False
        }
    }]

    try:
        async with config.COLLECTION.watch(pipline) as stream:
            async for change in stream:
                message = change["error"]
                await hendler.send_notification(message)

    except Exception as e:
        logging.log(level=logging.ERROR, msg=f"Error conn db: {e}")
