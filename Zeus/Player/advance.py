import os
import asyncio
import sys
import git
import heroku3
from Zeus.main import BOT
from config import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
hl = '/'
deadlyversion = 'Spambot0.10'

ZAID_PIC = "https://telegra.ph/file/7262dbb16274f074764b4.jpg"
  

DEADLY = "✯ 𝐌𝐮𝐬𝐢𝐜+𝐑𝐚𝐢𝐝 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.1`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **vᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   

                                  
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
     await BOT.send_file(event.chat_id,
                                  ZAID_PIC,
                                  caption=DEADLY,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/about_zeus_xd"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/TheMKHackerX131")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/zeusop5/AyanoMusic-2")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"╰•★✰  ℘ơŋɠ ✰★•╯\n\n⚘  ʂ℘ɛɛɖ : `{ms}`\n ⚘  ų℘ɬıɱɛ : 15h:6m:34s\n⚘  ơῳŋɛཞ : ⏤͟͞★𓆩᪵𝐙𝐄𝐔𝐒 𓆩𝐗𝐃𓆪 🥀\n✰ 𝐴𝑌𝐴𝑁𝑂 𝑀𝑈𝑆𝐼𝐶 𝐼𝑆 𝐴𝐿𝐼𝑉𝐸 ✰")
        
    

@BOT.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Rebooting ↪️**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await BOT.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

# this Feature Will Works only If u r Added Heroku api
@BOT.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        DEADLY = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[DEADLY] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
