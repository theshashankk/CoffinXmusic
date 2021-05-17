import requests
from CoffinXMusic.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from CoffinXMusic.services.callsmusic import run
from pyrogram import Client as Bot

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="CoffinXMusic.modules"),
)

bot.start()
run()
