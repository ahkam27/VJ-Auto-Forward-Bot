from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b5896515e659e119350a9d4ebaa5b732")
      API_ID = int(getenv("API_ID", "27737752"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else false
      BOT_TOKEN = getenv("BOT_TOKEN", "7975490214:AAEqgE1vY21n_RblldoYcUgNKJGIxazndA8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002066777216:-1002969803730").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
