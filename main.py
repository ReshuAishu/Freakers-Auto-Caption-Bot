import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", '4011894'))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", '56ac06547b5d8af50493e104feed8053')
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", '1736163316:AAEkXROTw-c3nAp-LsxWGMaWeTmLpRXGEpI')
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "<b>ᴛɪᴛʟᴇ:</b> <code>{file_name}</code>\n▬▬▬▬▬▬▬▬▬▬▬▬\n🍃<b><i>ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ</b></i>🍃\n<i>https://t.me/+HxPeOzEU3nlmMTdl</i>\n🍃<b><i>sᴇʀɪᴇs ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ</b></i>🍃\n<i>https://t.me/+4NvHgqi9_FRhNjY1</i>\n▬▬▬▬▬▬▬▬▬▬▬▬\n☘𝙅𝙤𝙞𝙣:-<b><i>https://t.me/Freakers_Filmy</b></i>\n\n🧐𝙁𝙧𝙚𝙖𝙠𝙚𝙧𝙨🎭𝙁𝙞𝙡𝙢𝙮™🍿©\n100% ғᴀꜱᴛ & ϙᴜᴀʟɪᴛʏ\n▬▬▬▬▬▬▬▬▬▬▬▬")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBot = pyrogram.Client(
   name="AutoCaptionBot", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋Hello {}</b>
<b>I am an AutoCaption bot</b>
<b>All you have to do is add me to your channel and I will show you my power</b>
<b>@freakersfilmy</b>"""

about_message = """
<b><i>ᴍʏ ɴᴀᴍᴇ : [ғʀᴇᴀᴋᴇʀs ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ](t.me/{username})\n
ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://www.instagram.com/naughty__nonsense/>ᴍᴀɴᴀғ</a>\n
ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ : <a href=https://t.me/Freakers_Filmy>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/+HxPeOzEU3nlmMTdl>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
sᴇʀɪᴇs ɢʀᴏᴜᴘ : <a href=https://t.me/FF_Series_Only>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
sᴇʀɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/+4NvHgqi9_FRhNjY1>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
sᴇʀɪᴇs ʙᴏᴛ  : <a href=https://t.me/ffseriesbot>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
18+ ʙᴏᴛ : <a href=https://t.me/A4_Adultsbot>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3\n
ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ\n
ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://railway.app/>ʀᴀɪʟᴡᴀʏ</a>\n
sᴏᴜʀᴄᴇ  : <a href=https://github.com/>ɢɪᴛʜᴜʙ</a>\n</i></b>
"""

@AutoCaptionBot.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  motech, _ = get_file_details(update)
  try:
      try: update.edit(custom_caption.format(file_name=motech.file_name))
      except pyrogram.errors.FloodWait as FloodWait:
          asyncio.sleep(FloodWait.value)
          update.edit(custom_caption.format(file_name=motech.file_name))
  except pyrogram.errors.MessageNotModified: pass 
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("𝑴𝒚 𝑮𝒓𝒐𝒖𝒑🍃", url="t.me/Freakers_Filmy"),
   pyrogram.types.InlineKeyboardButton("𝑨𝒃𝒐𝒖𝒕 𝑴𝒆🤗", callback_data="about")
   ],[
   pyrogram.types.InlineKeyboardButton("𝑨𝒅𝒅 𝑴𝒆 𝒀𝒐𝒖𝒓 𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url=f"http://t.me/{bot.username}?startchannel=true")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
  buttons = [[
   pyrogram.types.InlineKeyboardButton("𝑩𝒂𝒄𝒌 𝑻𝒐 𝑯𝒐𝒎𝒆", callback_data="start")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

print("Telegram AutoCaption V1 Bot Start")
print("Bot Created By https://t.me/Freakers_Filmy")

AutoCaptionBot.run()
