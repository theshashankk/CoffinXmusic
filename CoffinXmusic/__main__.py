import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN,BG_IMAGE


response = requests.get(BG_IMAGE)
file = open("./etc/cofin.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="CoffinXmusic.modules"),
)

bot.start()
run()
