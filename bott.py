

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import ParseMode


import logging
import os
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv("SECRETARY_BOT_TOKEN")

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

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    photo_file = open('venus.jpg', 'rb')
    keyboard =  [[InlineKeyboardButton("Get started on Venus.io", url="https://venus.io")],
                [InlineKeyboardButton("About Venus Protocol", callback_data='about')],
                [InlineKeyboardButton("Native token is $XVS", callback_data='xvs')],
                [InlineKeyboardButton("Venus Telegram Group", url="https://t.me/venusprotocol")],
                [InlineKeyboardButton("Venus Language Groups", callback_data='groups')],
                [InlineKeyboardButton("Venus Protocol on YouTube", callback_data='youtube')],
                [InlineKeyboardButton("Updates and News", callback_data='updates')],
                [InlineKeyboardButton("FAQ Venus Protocol", callback_data='faq')],
                [InlineKeyboardButton("Venus All Social Media Links", url="https://linktr.ee/venusprotocol")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    mread = '<b>What is Venus Protocol?</b>\nVenus Protocol is the top algorithmic-based money market system on the BNB Chain, designed to enable completely decentralized finance-based lending and credit system for its users.'
    update.message.reply_photo(photo=photo_file, parse_mode=ParseMode.HTML)
    update.message.reply_text(mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    

def startt(update, context):
    photo_file = open('venus.jpg', 'rb')
    keyboard =  [[InlineKeyboardButton("Get started on Venus.io", url="https://venus.io")],
                [InlineKeyboardButton("About Venus Protocol", callback_data='about')],
                [InlineKeyboardButton("Native token is $XVS", callback_data='xvs')],
                [InlineKeyboardButton("Venus Telegram Group", url="https://t.me/venusprotocol")],
                [InlineKeyboardButton("Venus Language Groups", callback_data='groups')],
                [InlineKeyboardButton("Venus Protocol on YouTube", callback_data='youtube')],
                [InlineKeyboardButton("Updates and News", callback_data='updates')],
                [InlineKeyboardButton("FAQ Venus Protocol", callback_data='faq')],
                [InlineKeyboardButton("Venus All Social Media Links", url="https://linktr.ee/venusprotocol")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    mread = '<b>What is Venus Protocol?</b>\nVenus Protocol is the top algorithmic-based money market system on the BNB Chain, designed to enable completely decentralized finance-based lending and credit system for its users.'
    query.edit_message_text(text=mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)
#    query.edit_reply_photo(photo=photo_file, caption=mread, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


def about_menu(update, context):
    keyboard = [[InlineKeyboardButton("Community Forum (Proposal ideas and discussions)", url='https://community.venus.io/')],
                [InlineKeyboardButton("Audits", callback_data='audits')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Welcome to the About menu. Please select an option.", reply_markup=reply_markup, parse_mode=ParseMode.HTML)

def audits_menu(update, context):
    keyboard = [[InlineKeyboardButton("CertiK Audit of Venus Protocol", url='https://docs.venus.io/docs/security#introduction')],
                [InlineKeyboardButton("PeckShield Audit of Venus Protocol", url='https://github.com/peckshield/publications/blob/master/audit_reports/PeckShield-Audit-Report-VenusGrant-v1.0.pdf')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Welcome to the Audits menu. To review the details, please select an option.", reply_markup=reply_markup, parse_mode=ParseMode.HTML)
    
def xvs_menu(update, context):
    keyboard = [[InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    mxvs = "Users can use XVS for Venus Protocol DAO governance and also earn various rewards by staking their XVS in the Venus Protocol's vault and protocol"
    contract = "<code>0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63</code>"
    query.edit_message_text(text=mxvs + "\n\n <b>XVS contract address</b> 👇\n" + contract, reply_markup=reply_markup, parse_mode="HTML")


def support_menu(update, context):
    keyboard = [[InlineKeyboardButton("Destek 1", callback_data='support1')],
                [InlineKeyboardButton("Destek 2", callback_data='support2')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Destek menüsüne hoş geldiniz. Lütfen bir seçenek seçin.", reply_markup=reply_markup)

def group1_menu(update, context):
    keyboard = [[InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Destek menüsüne hoş geldiniz. Lütfen bir seçenek seçin.", reply_markup=reply_markup)

def groups_menu(update, context):
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

                [InlineKeyboardButton("group1", callback_data='group1')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Destek menüsüne hoş geldiniz. Lütfen bir seçenek seçin.", reply_markup=reply_markup)

def youtube_menu(update, context):
    keyboard = [[InlineKeyboardButton("📹 User Guide", url='https://youtu.be/LSUVdSDSw2g')],
                [InlineKeyboardButton("📹 Vault [Stake - Withdraw]", url='https://youtu.be/XQEjGTUyMrw')],
                [InlineKeyboardButton("📹 Supply & Borrow", url='https://youtu.be/iU2MUI4k6Ws')],
                [InlineKeyboardButton("📹 Liquidation", url='https://youtu.be/1oZ-iQlWMDQ')],
                [InlineKeyboardButton("English Playlist", url='https://youtube.com/playlist?list=PLcxhLxBPFSXxuyTQkSPhiXZpOeqVIOKpE')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    myoutube = 'Welcome to the Youtube menu.<b>. Please select an option</b>\n'
    query.edit_message_text(text=myoutube, reply_markup=reply_markup, parse_mode=ParseMode.HTML)


def updates_menu(update, context):
    keyboard = [[InlineKeyboardButton("Venus 2023 Community Survey Results", callback_data='https://community.venus.io/t/2023-community-survey-results/3242')],
                [InlineKeyboardButton("More Updates..", url='https://community.venus.io/')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Destek menüsüne hoş geldiniz. Lütfen bir seçenek seçin.", reply_markup=reply_markup)



def faq_menu(update, context):
    keyboard =  [[InlineKeyboardButton("Destek 1", callback_data='support1')],
                [InlineKeyboardButton("How To Use Venus Guide?", url='https://medium.com/venusprotocol/how-to-use-venus-protocol-71cb09703fbf')],
                [InlineKeyboardButton("How to Use Venus Protocol Mini Program on Binance App", url='https://medium.com/venusprotocol/how-to-use-venus-protocol-mini-program-on-binance-app-226b76a85312')],
                [InlineKeyboardButton("How to setup BNB Chain on MetaMask?", url='https://medium.com/venusprotocol/venus-protocol-main-network-launched-52ea9929091f')],
                [InlineKeyboardButton("How to use XVS Vault? How to stake XVS?", url='https://medium.com/@Venus_protocol/venus-vault-user-guide-cd1042b18401')],
                [InlineKeyboardButton("How do liquidations work? 'Liquidation guide for Venus protocol'", url='https://community.venus.io/t/liquidation-guide-for-venus-protocol/2930')],
                [InlineKeyboardButton("How to use Venus for lending or borrowing?", url='https://youtu.be/ZZMFM1gYFNw')],
                [InlineKeyboardButton("Back", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.edit_message_text(text="Destek menüsüne hoş geldiniz. Lütfen bir seçenek seçin.", reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    if query.data == 'about':
        about_menu(update, context)
    elif query.data == 'xvs':
        xvs_menu(update, context)
    elif query.data == 'groups':
        groups_menu(update, context)
    elif query.data == 'youtube':
        youtube_menu(update, context)
    elif query.data == 'faq':
        faq_menu(update, context)
    elif query.data == 'updates':
        updates_menu(update, context)
    elif query.data == 'back':
        startt(update, context)
    
    elif query.data == 'group1':
        group1(update, context)
    elif query.data == 'group2':
        group2(update, context)
    elif query.data == 'group3':
        group3(update, context)

    else:
        query.answer()
        query.edit_message_text(text="Bu bir test.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()