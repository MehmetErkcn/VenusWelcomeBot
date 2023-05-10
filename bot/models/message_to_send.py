class MessageToSend:
    def __init__(self, message: str, to_chat_id: int, to_user_id: int = None):
        self.message = message
        self.to_chat_id = to_chat_id
        self.to_user_id = to_user_id
