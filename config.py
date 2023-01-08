## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2"BQBJRSwJY7HEFM8goF5sIvLccDLKmlqKNh7j_caAgT-YG38s6fgLlZlaZ32KVYV424k0LH0PMBhWVY-ow4szOiQMhSDcqcu9AsrTQWVOpf62DGkjyUEelMXZzRfVi-sBlUadyVio-LYdv_u2V3IHeHM7F8xjHkIfhxlMVK9j1Bt9yh18L6m0LNiPRdQh6ATp6jUeWqwVgFahFdjjQ73Ibs0dnYgkD6QqqrPWTqzPEBfr-U7nwarBpVz7ZP6vF7oLU-jxAKcVHTbMI3URVeK8BCvs4tbGtNRmn9KMWsh0-2pdSoBHjY0UlmU1PCswWdYo8OQ7_3QL2p5SZNzblyrYVCwhAAAAAVzBZK8A)).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "24782565"))
API_HASH = getenv("API_HASH", "cc4dff9c4deb8b1432cb59194124ddcb")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://vcbot:vcbot@cluster0.yqipgxg.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "harsh")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Harshmahimusic")
ALIVE_NAME = getenv("ALIVE_NAME", "harsh")
BOT_USERNAME = getenv("BOT_USERNAME", "harshmahi_musicbot")
OWNER_ID = getenv("OWNER_ID", "5851145391")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "harsh_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "alone_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "alone_support")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5851145391").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
