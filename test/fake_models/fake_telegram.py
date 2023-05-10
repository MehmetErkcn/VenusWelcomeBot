from test.fake_models.models import User, Message, Update, ChatMember, ChatMemberUpdated, Chat

def getUser() -> User:
    user = User.get()
    return user


def getMessage() -> Message:
    return Message.get()

def getChat() -> Chat:
    return Chat.get()

def getUpdate() -> Update:
    return Update.get()

def getChatMember() -> ChatMember:
    return ChatMember.get()

def getChatMemberUpdated() -> ChatMemberUpdated:
    return ChatMemberUpdated.get()