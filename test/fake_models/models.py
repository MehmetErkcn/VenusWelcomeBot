from datetime import datetime


class Message:
    def get():
        result = {}
        result['message_id'] = None
        result['from_user'] = User.get()
        result['chat'] = Chat.get()
        result['date'] = datetime.date
        result['text'] = None
        return result

class User:
    def get():
        result = {}
        result['first_name'] = None
        result['last_name'] = None
        result['username'] = None
        result['id'] = None
        result['is_bot'] = None
        return result

class Update:
    def get():
        result = {}
        result['message'] = None
        result['update_id'] = 1
        result['chat_member'] = None
        result['effective_user'] = User.get()
        return result

class Chat:
    def get():
        result = {}
        result['name'] = None
        result['id'] = None
        return result

class ChatMemberUpdated:
    def get():
        result = {}
        result['chat'] = Chat.get()
        result['from_user'] = User.get()
        result['date'] = datetime.date
        result['old_chat_member'] = ChatMember.get()
        result['new_chat_member'] = ChatMember.get()
        return result

class ChatMember:
    def get():
        result = {}
        result['user'] = User()
        result['status'] = None
        result['is_member'] = None
        return result
        