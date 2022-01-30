from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN","5220279497:AAGMFVQ-OE0fQrwBvnPhc31qA2_Rb0eU69s")
API_ID = int(getenv("API_ID", "11259645"))
API_HASH = getenv("API_HASH","2a0091696eecde4ae7c3f76cbf848c53")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "90"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Music:Music@cluster0.f9x4i.mongodb.net/Cluster0?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1960524560").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5197927958").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001776335996"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","मैं𝐍𝚃A͜͡ Ꮮ𝐈ᑕ 🇮🇳")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP"))


if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
