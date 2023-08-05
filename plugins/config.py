from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("29028317"))
API_HASH = getenv("8f2831819e4f3fdc44945d2e4d2aa095")

BOT_TOKEN = getenv("6350282310:AAFxYriYLz10BELXn92jZ0zi5FjPPSxDSdw")
OWNER_ID = int(getenv("5848055044"))

MONGO_DB_URI = getenv("64cd0227652c571ae5e11041")
MUST_JOIN = getenv("@T_R_KY4", None)
