import unittest
from bot.message_parser import MessageParser
from test.fake_models.fake_telegram import *



class Test(unittest.TestCase):
    def testNoExceptionOnNonJoin(self):
        update: Update = getUpdate()
        MessageParser.getMessages(update)
    
    def testUserHasNullUsername(self):
        update = getUpdate()
        update['message'] = {}
        user = getUser()
        user["first_name"] = "test"
        user["last_name"] = "testington"
        update['message']['new_chat_members'] = [
            user
        ]

        update['message']['chat'] = {}
        update['message']['chat']['id'] = 123
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 1)
        assert("test testington" in messages[0].message)
    
    def testMessageSentOnJoin(self):
        update = getUpdate()
        update['message'] = {}
        user = getUser()
        user["first_name"] = "test"
        user["last_name"] = "testington"
        user["username"] = "testy"
        update['message']['new_chat_members'] = [
            user
        ]

        update['message']['chat'] = {}
        update['message']['chat']['id'] = 123
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 1)
        assert("test testington" in messages[0].message)
        assert((not 'testy' in messages[0].message))
    
    def testMessageNotSentOnNonJoinUpdate(self):
        update = getUpdate()
        update['message'] = {"text": "Hello guys!"}
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 0)
        