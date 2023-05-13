# -*- coding: utf-8 -*-

import logging
from typing import Tuple
from telegram import __version__ as TG_VER
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram import ChatPermissions, ChatMemberUpdated, ChatMember
from telegram.ext import ChatMemberHandler
from telegram.ext import CallbackContext
import asyncio

import time
import os
from dotenv import load_dotenv
from warnings import filterwarnings
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)

from telegram.warnings import PTBUserWarning

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

log_file = '/bots/venuswelcome/welcomelog.log'

# Enable logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
handler = logging.FileHandler(log_file, encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging.getLogger('').addHandler(handler)

#logging.info('Starting')

# Stages
START_ROUTES, END_ROUTES = range(2)
# Callback data
welcome, startt, about, audits, xvs, groups, youtube, faq, updates, back, tutorial = range(11)

# Create an empty dictionary to store new members' names and status
new_members = {}
groupid = 1
messageid = 1


load_dotenv()
TOKEN = os.getenv("SECRETARY_BOT_TOKEN")

deletetime= os.getenv("deletetime")

group1= os.getenv("group1")
group2= os.getenv("group2")
group3= os.getenv("group3")
group4= os.getenv("group4")
group5= os.getenv("group5")
group6= os.getenv("group6")
group7= os.getenv("group7")
group8= os.getenv("group8")
group9= os.getenv("group9")
group10= os.getenv("group10")
group11= os.getenv("group11")
group12= os.getenv("group12")
group13= os.getenv("group13")
group14= os.getenv("group14")
group15= os.getenv("group15")
group16= os.getenv("group16")
group17= os.getenv("group17")
group18= os.getenv("group18")
group19= os.getenv("group19")
group20= os.getenv("group20")

urlgroup1= os.getenv("urlgroup1")
urlgroup2= os.getenv("urlgroup2")
urlgroup3= os.getenv("urlgroup3")
urlgroup4= os.getenv("urlgroup4")
urlgroup5= os.getenv("urlgroup5")
urlgroup6= os.getenv("urlgroup6")
urlgroup7= os.getenv("urlgroup7")
urlgroup8= os.getenv("urlgroup8")
urlgroup9= os.getenv("urlgroup9")
urlgroup10= os.getenv("urlgroup10")
urlgroup11= os.getenv("urlgroup11")
urlgroup12= os.getenv("urlgroup12")
urlgroup13= os.getenv("urlgroup13")
urlgroup14= os.getenv("urlgroup14")
urlgroup15= os.getenv("urlgroup15")
urlgroup16= os.getenv("urlgroup16")
urlgroup17= os.getenv("urlgroup17")
urlgroup18= os.getenv("urlgroup18")
urlgroup19= os.getenv("urlgroup19")
urlgroup20= os.getenv("urlgroup20")

#updater = Updater(token=TOKEN, use_context=True)
#dispatcher = updater.dispatcher


async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    print("welcome")
    """Greets new users in chats and announces when someone leaves"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
#    cause_name = update.chat_member.from_user.mention_html()
#    member_name = update.chat_member.new_chat_member.user.mention_html()
#    print(cause_name)
#    time.sleep(0.1)
#    print(member_name)
#    time.sleep(0.1)
#    new_member = update.chat_member.new_chat_member
#    query = update.callback_query
    username = update.chat_member.new_chat_member.user.username
#    print(new_member)
#    time.sleep(0.1)

    if not was_member and is_member:
#        print("katıldı")
#       Mute group
        try:
            await context.bot.restrict_chat_member(
            chat_id=update.chat_member.chat.id,
            user_id=update.chat_member.new_chat_member.user.id,
            permissions=ChatPermissions(can_send_messages=False))
        except BadRequest:
            pass

        keyboard = [
            [InlineKeyboardButton("Get Tutorial & Unmute Me", url=f"http://t.me/{context.bot.username}?start=tutorial")]
        ]
#       print("buton waiting")
#       print(f'Welcome @{username}!\nClick button to open Welcome Chat with Tutorials.')
        reply_markup = InlineKeyboardMarkup(keyboard)
        wmessage = await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Welcome @{username}!\nClick button to open Welcome Chat with Tutorials.', reply_markup=reply_markup, parse_mode=ParseMode.HTML)
#       print("deleting welcome")
        try:
#            time.sleep(0.1)
            await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            pass

        asyncio.create_task(wait_and_delete(context, wmessage.chat_id, wmessage.message_id, int(deletetime)))

        user = update.effective_user
        group = update.effective_chat
        logger.info("Username @%s name %s joined the group @%s", user.username, user.first_name, group.username)

#        for new_member in update.chat_member.new_chat_member:
        new_members[update.chat_member.new_chat_member.user.id] = True
        global groupid
        global messageid
        groupid = update.effective_chat.id
        messageid = wmessage.message_id
            
#       print(messageid)
#       print(groupid)
#       print(new_members)
    elif was_member and not is_member:
        pass
#       print("ayrıldı")


def extract_status_change(chat_member_update: ChatMemberUpdated) -> Tuple[bool, bool]:
    """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns a tuple of
    booleans indicating whether the member was in the group before and after the update.
    """
    old_status = chat_member_update.old_chat_member.status
    new_status = chat_member_update.new_chat_member.status
#    old_is_member = chat_member_update.old_chat_member.is_member
#    new_is_member = chat_member_update.new_chat_member.is_member
    try:
        new_is_member = chat_member_update.new_chat_member.is_member
    except:
        pass # hatayı görmezden gelmek için hiçbir şey yapmayın

    try:
        old_is_member = chat_member_update.old_chat_member.is_member
    except:
        pass # hatayı görmezden gelmek için hiçbir şey yapmayın

    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)

    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    if not was_member and is_member:
#        print("New member joined the group") 
        pass
    elif was_member and not is_member:
#        print("Member left the group")
        pass
    elif was_member and is_member:
#        print("Member's status changed") 
        pass
    else:
#        print("Member is not a member of the group anymore") 
        pass

    return was_member, is_member

    
async def wait_and_delete(context: CallbackContext, chat_id: int, message_id: int, delay: int):
    await asyncio.sleep(delay)
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    photo_file = open('/bots/venuswelcome/venus.jpg', 'rb')
    user = update.message.from_user
    logger.info("User @%s %s started the conversation.", user.username, user.first_name)
    keyboard =  [[InlineKeyboardButton("Get started on Venus.io", url="https://venus.io")],
                [InlineKeyboardButton("About Venus Protocol", callback_data=str(about))],
                [InlineKeyboardButton("Native token is $XVS", callback_data=str(xvs))],
                [InlineKeyboardButton("Venus Telegram Group", url="https://t.me/venusprotocol")],
                [InlineKeyboardButton("Venus Language Groups", callback_data=str(groups))],
                [InlineKeyboardButton("Venus Protocol on YouTube", callback_data=str(youtube))],
                [InlineKeyboardButton("Updates and News", callback_data=str(updates))],
                [InlineKeyboardButton("FAQ Venus Protocol", callback_data=str(faq))],
                [InlineKeyboardButton("Venus All Social Media Links", url="https://linktr.ee/venusprotocol")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mread = '<b>What is Venus Protocol?</b>\nVenus Protocol is the top algorithmic-based money market system on the BNB Chain, designed to enable completely decentralized finance-based lending and credit system for its users.'
    await update.message.reply_html(mread, reply_markup=reply_markup)
    
    user = update.message.from_user
    id = user.id
    if id in new_members and new_members[id]:
        # If the user is in the dictionary and their status is True, unmute them
        try:
            await context.bot.delete_message(chat_id=groupid, message_id=messageid)
#            print("silindi")
        except:
            pass
        
        try:
            await context.bot.restrict_chat_member(
            chat_id=groupid,
            user_id=user.id,
            permissions=ChatPermissions(can_send_messages=True))
            logger.info("User @%s %s started the conversation and unmuted.", user.username, user.first_name)
        except BadRequest:
            pass
        new_members[id] = False
    #update.message.reply_photo(photo=photo_file, parse_mode=ParseMode.HTML)
    #update.message.reply_text(mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    return START_ROUTES


async def startt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
#    photo_file = open('/bots/venuswelcome/venus.jpg', 'rb')
    keyboard =  [[InlineKeyboardButton("Get started on Venus.io", url="https://venus.io")],
                [InlineKeyboardButton("About Venus Protocol", callback_data=str(about))],
                [InlineKeyboardButton("Native token is $XVS", callback_data=str(xvs))],
                [InlineKeyboardButton("Venus Telegram Group", url="https://t.me/venusprotocol")],
                [InlineKeyboardButton("Venus Language Groups", callback_data=str(groups))],
                [InlineKeyboardButton("Venus Protocol on YouTube", callback_data=str(youtube))],
                [InlineKeyboardButton("Updates and News", callback_data=str(updates))],
                [InlineKeyboardButton("FAQ Venus Protocol", callback_data=str(faq))],
                [InlineKeyboardButton("Venus All Social Media Links", url="https://linktr.ee/venusprotocol")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mread = '<b>What is Venus Protocol?</b>\nVenus Protocol is the top algorithmic-based money market system on the BNB Chain, designed to enable completely decentralized finance-based lending and credit system for its users.'
    await query.edit_message_text(mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
#    query.edit_reply_photo(photo=photo_file, caption=mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


async def about_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("Community Forum (Proposal ideas and discussions)", url='https://community.venus.io/')],
                [InlineKeyboardButton("Audits", callback_data=str(audits))],
                [InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text="Welcome to the About menu. <b>Please select an option..</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    return START_ROUTES

async def audits_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("CertiK Audit of Venus Protocol", url='https://docs.venus.io/docs/security#introduction')],
                [InlineKeyboardButton("PeckShield Audit of Venus Protocol", url='https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-VenusGrant-v1.0.pdf')],
                [InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text="Welcome to the Audits menu. <b>Please select an option..</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
async def xvs_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mxvs = "Users can use <b>$XVS</b> for Venus Protocol DAO governance and also earn various rewards by staking their <b>$XVS</b> in the Venus Protocol's vault and protocol"
    contract = "<code>0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63</code>"
    await query.edit_message_text(text=mxvs + "\n\n <b>XVS contract address</b> \U0001F447\n" + contract, reply_markup=reply_markup, parse_mode="HTML")


async def groups_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard =[[InlineKeyboardButton(group1, url=urlgroup1),
                InlineKeyboardButton(group2, url=urlgroup2)],
                [InlineKeyboardButton(group3, url=urlgroup3),
                InlineKeyboardButton(group4, url=urlgroup4)],
                [InlineKeyboardButton(group5, url=urlgroup5),
                InlineKeyboardButton(group6, url=urlgroup6)],
                [InlineKeyboardButton(group7, url=urlgroup7),
                InlineKeyboardButton(group8, url=urlgroup8)],
                [InlineKeyboardButton(group9, url=urlgroup9),
                InlineKeyboardButton(group10, url=urlgroup10)],
                [InlineKeyboardButton(group11, url=urlgroup11),
                InlineKeyboardButton(group12, url=urlgroup12)],
                [InlineKeyboardButton(group13, url=urlgroup13),
                InlineKeyboardButton(group14, url=urlgroup14)],
                [InlineKeyboardButton(group15, url=urlgroup15),
                InlineKeyboardButton(group16, url=urlgroup16)],
                [InlineKeyboardButton(group17, url=urlgroup17),
                InlineKeyboardButton(group18, url=urlgroup18)],
                [InlineKeyboardButton(group19, url=urlgroup19),
                InlineKeyboardButton(group20, url=urlgroup20)],
                [InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Welcome to the Groups menu. <b>Please select an option..</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)

async def youtube_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("\U0001F4F9 User Guide", url='https://youtu.be/LSUVdSDSw2g')],
            [InlineKeyboardButton("\U0001F4F9 Vault [Stake - Withdraw]", url='https://youtu.be/XQEjGTUyMrw')],
            [InlineKeyboardButton("\U0001F4F9 Supply & Borrow", url='https://youtu.be/iU2MUI4k6Ws')],
            [InlineKeyboardButton("\U0001F4F9 Liquidation", url='https://youtu.be/1oZ-iQlWMDQ')],
            [InlineKeyboardButton("\U0001F4C3 English Playlist", url='https://youtube.com/playlist?list=PLcxhLxBPFSXxuyTQkSPhiXZpOeqVIOKpE')],
            [InlineKeyboardButton("\U0001F519 Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    myoutube = 'Welcome to the Youtube menu.<b>. Please select an option..</b>\n'
    await query.edit_message_text(text=myoutube, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


async def updates_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("Venus 2023 Community Survey Results", url='https://community.venus.io/t/2023-community-survey-results/3242')],
                [InlineKeyboardButton("More Updates..", url='https://community.venus.io/')],
                [InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Welcome to Updates and News menu. <b>Please select an option..</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)


async def faq_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    keyboard =  [
                [InlineKeyboardButton("How To Use Venus Guide?", url='https://medium.com/venusprotocol/how-to-use-venus-protocol-71cb09703fbf')],
                [InlineKeyboardButton("How to Use Venus Protocol Mini Program on Binance App", url='https://medium.com/venusprotocol/how-to-use-venus-protocol-mini-program-on-binance-app-226b76a85312')],
                [InlineKeyboardButton("How to setup BNB Chain on MetaMask?", url='https://medium.com/venusprotocol/venus-protocol-main-network-launched-52ea9929091f')],
                [InlineKeyboardButton("How to use XVS Vault? How to stake XVS?", url='https://medium.com/@Venus_protocol/venus-vault-user-guide-cd1042b18401')],
                [InlineKeyboardButton("How do liquidations work? 'Liquidation guide for Venus protocol'", url='https://community.venus.io/t/liquidation-guide-for-venus-protocol/2930')],
                [InlineKeyboardButton("How to use Venus for lending or borrowing?", url='https://youtu.be/ZZMFM1gYFNw')],
                [InlineKeyboardButton("Back", callback_data=str(back))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Welcome to FAQ menu. <b>Please select an option..</b>", reply_markup=reply_markup, parse_mode=ParseMode.HTML)

#async def tutorial(update: Update, context: CallbackContext):
    # Grup mesajini sil
#    await context.bot.delete_message(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
    
#start_handler = CommandHandler('start', start)
#dispatcher.add_handler(start_handler)
#updater.dispatcher.add_handler(CallbackQueryHandler(button))
#updater.start_polling()
#updater.idle()

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    bot = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram

#S    bot.add_handler(CommandHandler("help", help_command))
#    bot.add_handler(ChatMemberHandler(filters.status_update.new_chat_members, welcome))
#    bot.add_handler(ChatMemberHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
    # Handle members joining/leaving chats.
    bot.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
#    bot.add_handler(CallbackQueryHandler(tutorial, pattern=r'^tutorial\|.*$'))

    # on non command i.e message - echo the message on Telegram
#    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(about_menu, pattern="^" + str(about) + "$"),
                CallbackQueryHandler(xvs_menu, pattern="^" + str(xvs) + "$"),
                CallbackQueryHandler(groups_menu, pattern="^" + str(groups) + "$"),
                CallbackQueryHandler(youtube_menu, pattern="^" + str(youtube) + "$"),
                CallbackQueryHandler(faq_menu, pattern="^" + str(faq) + "$"),
                CallbackQueryHandler(updates_menu, pattern="^" + str(updates) + "$"),
                CallbackQueryHandler(audits_menu, pattern="^" + str(audits) + "$"),
                CallbackQueryHandler(startt, pattern="^" + str(back) + "$"),   
            ],
            END_ROUTES: [
                CallbackQueryHandler(startt, pattern="^" + str(back) + "$"),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
        #per_message=True  # burada per_message parametresi True olarak ayarlan?yor.
    )

    # Add ConversationHandler to application that will be used for handling updates
    bot.add_handler(conv_handler)
    # Run the bot until the user presses Ctrl-C
    bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
