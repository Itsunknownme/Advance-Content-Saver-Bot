from os import environ 

class Config:
    API_ID = environ.get("API_ID", "21273907")
    API_HASH = environ.get("API_HASH", "6717e06be9458c10dfe4cbf9c9ce5cca")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6874124879:AAFrCVQUuHIwEdeU04FEhi9cCsGq9VDuhHo") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5633810208').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
