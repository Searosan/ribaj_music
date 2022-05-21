import asyncio

from plugins import LOGS
from pytgcalls import idle
from config import BOT_USERNAME as cli
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    LOGS.info("[INFO]: BOT & ANIEUSERBOT CLIENT STARTED !!")
    await calls.start()
    LOGS.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("osmanigroupbot")
    await user.join_chat("teamosmani")
    await user.send_message(f"{cli}", "/start")
    await idle()
    LOGS.info("[INFO]: BOT & USERBOT STOPPED !!")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
