# Leo Projects <https://t.me/leosupportx>
# @Naviya2 🇱🇰

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from LeoSongDownloaderBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LeoSongDownloaderBot import LeoSongDownloaderBot as app
from LeoSongDownloaderBot import LOGGER

pm_start_text = """
Hello [{}](tg://user?id={}) 👋

I'm Leo Song Downloader Bot 🇱🇰

You can download any song within a shortime with this Bot 🙂

If you want to know how to use this bot just
touch on this command " /help " 🙂

Leo Projects 🇱🇰
"""

help_text = """
You should know the following commands to use this bot 🙂

⭕️ /song <song name>: Download songs from all sources 😏

⭕️ Send youtube url to me directly i can download it to your telegram database in audio format 🙂


Made By : @cokepokess
Support Group : @Adam_hakli
Updates Channel : @cokepokess
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         text="Updates Channel🗣", url="https://t.me/new_ehi"
                    ),
                    InlineKeyboardButton(
                        text="Support Group👥", url="https://t.me/leosupportx"
                    ),
                ],
                    
                [
                    InlineKeyboardButton(
                        text="Developer🧑‍💻", url="https://t.me/naviya2"
                    ),
                    InlineKeyboardButton(
                        text="Rate us ★", url="https://t.me/tlgrmcbot?start=leosongdownloaderbot-review"
                    ),     
                ],
                
                [
                    InlineKeyboardButton(
                        text="➕ Add me to your group ➕", url="t.me/leosongdownloaderbot?startgroup=true"
                    ),
                ],
            ],
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("LeoSongDownloaderBot is online.")
idle()
