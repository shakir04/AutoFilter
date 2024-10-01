from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
import requests, os


API = "https://apis.xditya.me/lyrics?song="

@Client.on_message(filters.text & filters.command(["lyrics"]))
async def sng(bot, message):
        if not message.reply_to_message:
          await message.reply_text("Pʟᴇᴀꜱᴇ Rᴇᴩʟʏ To A Mᴇꜱꜱᴀɢᴇ")
        else:          
          mee = await message.reply_text("`Sᴇᴀʀᴄʜɪɴɢ 🔎`")
          song = message.reply_to_message.text
          chat_id = message.from_user.id
          rpl = lyrics(song)
          await mee.delete()
          try:
            await mee.delete()
            await bot.send_message(chat_id, text = rpl, reply_to_message_id = message.id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/paid_method_zone")]]))
          except Exception as e:                            
             await message.reply_text(f"I Cᴀɴ'ᴛ Fɪɴᴅ A Sᴏɴɢ Wɪᴛʜ `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url = f"t.me/paid_method_zone")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Sᴜᴄᴄᴇꜱꜰᴜʟʟy Exᴛʀᴀᴄᴛᴇᴅ Lyɪʀɪᴄꜱ Oꜰ {song}**\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**Mᴀᴅᴇ Bʏ AI**'
        return text
