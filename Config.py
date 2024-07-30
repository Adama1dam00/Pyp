# Requier Modules
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import logging, time, sys, os



# Bot Configs 
class config:
    SESSION = "<PYROGRAM_SESSION>" # This Is Pyrogram Session Hers
    API_KEY = "<7476174611:AAE2ll_6ScgUwAAqqk9QdP-7YqoUffTBdec>" # This is Bot API Key
    AUTH = 5780100639 # Sudo id
    FORCESUB = '<CHANNLS>' # Public Channls
    
    API_ID = 20979355 
    API_HASH = "6dee6a94ee1d8ddf0ae38a35167ce8ba"
    SUDO_USERS = set() # Admins List 


# Check Bot File Exists 
if not os.path.exists('./.sessions'):
    os.mkdir('./.sessions')


bot = TelegramClient('./.sessions/rad', config.API_ID, config.API_HASH).start(bot_token=config.API_KEY) 
userbot = Client("myacc",api_id=config.API_ID,api_hash=config.API_HASH,session_string=config.SESSION)

try:
    userbot.start()
except BaseException:
    sys.exit(1)


Bot = Client(
    "./.sessions/SaveRestricted",
    bot_token=config.API_KEY,
    api_id=int(config.API_ID),
    api_hash=config.API_HASH
)    


try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
