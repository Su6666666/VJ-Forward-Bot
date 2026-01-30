# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "28777954"))
    API_HASH = environ.get("API_HASH", "fe8cc25e1bf6f0a6bf33df1588785880")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://SGBACKUP:SGBACKUP@cluster0.173ksrb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "919169586"))
    
    # Force Subscribe Logic (Only Added These)
    # আপনার চ্যানেলের আইডি এখানে দিন (যেমন: -100xxxxxxxx)
    AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1001877309572")) 
    # চ্যানেলের ইনভাইট লিংক (অপশনাল, বটের মেসেজে দেখানোর জন্য)
    REQ_CHANNEL = environ.get("REQ_CHANNEL", "https://t.me/sgbackup") 

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

