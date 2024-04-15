import os


class Config(object):
    APP_ID = os.environ.get("APP_ID", "13279715")
    API_HASH = os.environ.get("API_HASH", "56e198053932ecf216af72a2ddffcd78")
    TOKEN = os.environ.get("TOKEN", "7132821230:AAEuc3cf-VDDWnsODFZPYE4asmGkIyQXszo")
    BOT_US = os.environ.get("BOT_US", "Obanai_ixbot")
    WELCOME_TEXT = os.environ.get(
        "WELCOME_TEXT", "Cardinal System Is Damaged!, Sorry I Cant Remember You."
    )
    RULES = os.environ.get("RULES", "https://t.me/Programmer_Updates/8")
