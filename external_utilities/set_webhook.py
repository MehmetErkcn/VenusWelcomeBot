import telegram

print("provide token")
token = input()
print("provide webhook url (or no to use existing)")
url = input()

bot = telegram.Bot(token=token)

if url == "no":
    url = bot.get_webhook_info()['url']


bot.set_webhook(url, allowed_updates=["new_chat_members"]) and print("Successfully updated")
