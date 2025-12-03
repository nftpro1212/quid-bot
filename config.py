import os
import re
from dotenv import load_dotenv

# .env fayldan o'zgaruvchilarni yuklash
load_dotenv()

# Bot sozlamalari
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
SEND_TIME = os.getenv('SEND_TIME', '09:00')

# Xabar formatlash sozlamalari
MESSAGE = os.getenv('MESSAGE')
MESSAGE_INTRO = os.getenv('MESSAGE_INTRO', '')
_message_items_raw = os.getenv('MESSAGE_ITEMS', '')
MESSAGE_ITEMS = [
    item.strip()
    for item in re.split(r'[|;]', _message_items_raw)
    if item.strip()
]
MESSAGE_OUTRO = os.getenv('MESSAGE_OUTRO', '')
MENTION_ALL = os.getenv('MENTION_ALL', 'true').lower() in ('1', 'true', 'yes', 'ha')

# Sozlamalarni tekshirish
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylida topilmadi!")
if not CHAT_ID:
    raise ValueError("CHAT_ID .env faylida topilmadi!")
