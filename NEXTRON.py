import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
try:
  from userbot import devs, id, ID, LEGEND
except:
  os.system("pip install NEXTRON")
try:
  from NEXTRON import bot 
except:
  pass
from userbot import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("nextron", API_ID, API_HASH).start(bot_token=token)
import time
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "υℓтяα χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "υℓтяα χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
NEXTRON = "[NEXTRON](https://t.me/NEXTRONOP)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[υℓтяα χ вσт](https://github.com/majid-nex/nextron-bot)"

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/nextronsupport)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
