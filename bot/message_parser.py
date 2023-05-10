import os
from telegram import Bot, Update
from bot.models.message_to_send import MessageToSend
import random
from dotenv import load_dotenv

load_dotenv()

class MessageParser:
        # SECRETARY_BOT_TO_USER değerini alıyoruz
    to_user = os.getenv("SECRETARY_BOT_TO_USER")


    print(to_user)
    
    @staticmethod
    def get_message_string(username):
        random.seed()
        cand = []
        with open("config/responses.txt") as f:
            for line in f:
                cand.append(line)
        
        message_index = random.randrange(0, len(cand) - 1)

        message = cand[message_index]
        return message.replace("[target]", username) \
            .replace("[boss]", MessageParser.to_user)
    

    

#    @staticmethod
#    def getMessages(update) -> list[MessageToSend]:
#        result = []
#        if update.message and update.message.new_chat_members:
#            chat = update.message.chat
#            for user in update.message.new_chat_members:
#                name = MessageParser.getFullName(user)
#                user_id = update.message.new_chat_members[0].id
#                print(user_id)
#                message = MessageParser.get_message_string(name)
#                result.append(MessageToSend(chat['id'], message))
#        return result
    

    @staticmethod
    def getMessages(update) -> list[MessageToSend]:
        result = []
        if update.message and update.message.new_chat_members:
            chat = update.message.chat
            chat_id = chat['id']
            for user in update.message.new_chat_members:
                name = MessageParser.getFullName(user)
                user_id = user.id
                print(user_id)
                message = MessageParser.get_message_string(name)
                result.append(MessageToSend(user_id, message))
        return result

    @staticmethod

    
    def getFullName(user):
        result = ""
        if "first_name" in str(user):
            result += user["first_name"]
        elif "last_name" in user:
            return user["last_name"]
        
        if "last_name" in str(user):
            result += " " + user["last_name"]
        
        return result

