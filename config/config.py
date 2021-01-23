from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2920885
API_HASH = "c69f36c8f832bd7f69f87d91b31f046f"

# Get this from @Botfather
TOKEN = "1560221014:AAEgISXhopiNfcsQGEKXHFIzDtuTvDLGPpE"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = ""

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    697204915,
    989367338,
    720679955
]

# The ID of the group where your bot streams
GROUP = -1001309737901

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 100000

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
