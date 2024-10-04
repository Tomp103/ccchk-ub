from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("25731874"))
API_HASH = input("34f53a34140f370acde6d7e56b3f56b2") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
