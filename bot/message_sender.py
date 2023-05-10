from telegram import Bot
from bot.models.message_to_send import MessageToSend
import logging
import os
from dotenv import load_dotenv

load_dotenv()
cid = os.getenv("SECRETARY_BOT_TO_GROUP")

class MessageSender:

    def __init__(self):
        token=os.getenv("SECRETARY_BOT_TOKEN")
        if token == None:
            logging.exception("SECRETARY_BOT_TOKEN not defined")
        self.bot = Bot(token=token)
        
    def sendMessages(self, messages: list[MessageToSend]):
        for message in messages:
            self.sendMessage(message)
    
    def sendMessage(self, message: MessageToSend):
        print("Sending message to " + str(message.to_chat_id))
        try:
            self.bot.send_message(chat_id=message.message, text=message.to_chat_id)
            
        except BaseException as e:
            logging.warning("Could not send message to " + message.to_chat_id + "\n" + str(e))
            self.bot.send_message(chat_id=cid, text="Buna tıklayın - http://t.me/michalenbot?start=start")