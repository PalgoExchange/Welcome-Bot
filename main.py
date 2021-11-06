from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''𝙷𝚊𝚒 , \n\n𝙸𝚊𝚖  𝚊  𝚂𝚒𝚖𝚙𝚕𝚎  𝚆𝚎𝚕𝚌𝚘𝚖𝚎  𝙱𝚘𝚝.  𝙰𝚍𝚍  𝚖𝚎  𝚝𝚘  𝚢𝚘𝚞𝚛  𝚐𝚛𝚘𝚞𝚙  𝚊𝚗𝚍  𝚖𝚊𝚔𝚎  𝚖𝚎  𝚊𝚜  𝚊𝚍𝚖𝚒𝚗\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @DrQuant ''')

def help(updater,context):
 updater.message.reply_text("➠ 𝙰𝚍𝚍  𝙼𝚎  𝚃𝚘  𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎  𝙰𝚍𝚖𝚒𝚗  𝙼𝚎\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @DrQuant")\
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hi New palgian {member.full_name} , Welcome to Palgo Exchange official telegram community\n\n We share  information/activities daily to help you achieve more in your crypto journey. Please click on the pinned post at the top of this chat for our most recent update\n\n 🌟 If you do not have a Palgo account yet, please visit https://palgo.us to join our waitlist to get $25 worth of PALET airdrop.\n\n ⚠️ Lastly, do not reply DMs with unsolicited offers, they are most likely a scam. Palgo Admins will never PM you first. \n\n Thank You For Joining Palgo💖')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()

"""
Hello Q for Quant, welcome to Bybit Africa

We share  information/activities daily to help you achieve more in your crypto journey. Please click on the pinned post at the top of this chat for our most recent update

🌟 If you do not have a Bybit account yet, please click here (https://palgo.us/waitlist) to create an account. Here are some helpful articles (https://learn.bybit.com/bybit-guide/) and videos (https://learn.bybit.com/bybit-guide/videos/) on how to get started trading on Bybit. 

📚 We host technical analysis and crypto education sessions weekly, click here (https://t.me/BybitAfrica/75674) to learn more from the insightful sessions held previously.

📌 Pin this group to the top of your Telegram chats and let us know; if you could turn back the hands of time to 1 year earlier, what crypto would you buy and why? 😁

⚠️ Lastly, do not reply DMs with unsolicited offers, they are most likely a scam. Bybit Admins will never PM you first.
"""