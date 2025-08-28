from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError
import sqlite3
import re
import os
from dotenv import load_dotenv
from cachetools import cached, TTLCache
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import timedelta

load_dotenv()  # Загрузка секретных данных (.env file)

API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
PHONE_NUMBER = os.getenv('TELEGRAM_PHONE_NUMBER')
DB_NAME = os.getenv('DATABASE_NAME', 'posts.db')

GROUP_LINKS = ['@example_group']
INTERESTING_TAGS = {'#sport', '#cinema'}  # Измените на интересующие вас теги

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Создание таблицы (если не создана ранее)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT NOT NULL,
        post_url TEXT UNIQUE NOT NULL,
        hashtags TEXT DEFAULT ''
    );
''')

# ⚡️ Кэширование операций (уменьшаем нагрузку на API)
cache = TTLCache(maxsize=100, ttl=timedelta(hours=1))

@cached(cache)
def fetch_tags(message):
    """Получает все хэштеги из сообщения."""
    return set(re.findall(r'#\w+', message.text))

def parse_groups(client):
    for link in GROUP_LINKS:
        entity = client.get_entity(link)
        messages = client.iter_messages(entity, limit=100)
        
        for msg in messages:
            tags_in_msg = fetch_tags(msg)
            
            if INTERESTING_TAGS & tags_in_msg:
                cursor.execute(
                    "INSERT OR IGNORE INTO posts(post_url, chat_id, hashtags) VALUES(?, ?, ?)",
                    (msg.link, entity.id, ', '.join(tags_in_msg))
                )
                
    conn.commit()

def edit_image(image_path, text="Hello"):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=50)
    w, h = draw.textsize(text, font=font)
    x = (img.width - w) // 2
    y = (img.height - h) // 2
    draw.text((x, y), text, fill="white", font=font)
    
    return img

def process_and_send_post(msg_data):
    image_bytes = BytesIO(msg_data.media.document.bytes)
    edited_img = edit_image(image_bytes)
    
    output_buffer = BytesIO()
    edited_img.save(output_buffer, format='JPEG')
    output_buffer.seek(0)
    
    bot.send_photo(chat_id="@target_channel", photo=output_buffer, caption=msg_data.caption)

with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
    parse_groups(client)
