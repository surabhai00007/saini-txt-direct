#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22537641"))
API_HASH = environ.get("API_HASH", "6c1eee32be959812f0598919209a2105")
BOT_TOKEN = environ.get("BOT_TOKEN", "7260913766:AAGgpZlkc0Y6GBFEihJSaYfnYLl2V1Y9IXY")

OWNER = int(environ.get("OWNER", "5680454765"))
CREDIT = environ.get("CREDIT", "SARKARI नौकरी")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))


