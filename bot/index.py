import json
import bot.message_parser
import bot.message_sender
from telegram.update import Update

def handler(event, context):

    sender = bot.message_sender.MessageSender()
    sender.sendMessages(bot.message_parser.MessageParser.getMessages(json.loads(event['body'])))

    return {
        'statusCode': 200
    }