# cokepokes project <https://t.me/cokepokess>
# @Adam_Hakli

import os

import requests
import wget
from pyrogram import filters

from LeoSongDownloaderBot import LeoSongDownloaderBot

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@LeoSongDownloaderBot.on_message(filters.command("saavn"))
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("<b>Just send your song name with /song command</b>")
        return ""
    m = await message.reply_text(" Mahni Yuklenir ")
    try:
        r = requests.get(
            f"https://jevcplayerbot-saavndl.herokuapp.com/result/?query={args}"
        )
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["singers"]
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await m.edit("Uploading...")
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers)
    os.remove(ffile)
    await m.delete()
