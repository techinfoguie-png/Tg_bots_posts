# src/parsers.py
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

async def parse_groups(client):
    participants = await client(GetParticipantsRequest(channel='@test_group', q='', offset=0, filter=ChannelParticipantsSearch(''), hash=0))
    for participant in participants.users:
        print(participant.username)
#or this
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError
import sqlite3
import re

API_ID = 'your_api_id_here'
API_HASH = 'your_api_hash_here'
PHONE_NUMBER = '+your_phone_number'
GROUP_LINKS = ['@channel_name_or_link']
INTERESTING_TAGS = {'#спорт', '#кино'}

conn = sqlite3.connect('posts.db')
cursor = conn.cursor()

def parse_groups(client):
    for link in GROUP_LINKS:
        entity = client.get_entity(link)
        messages = client.iter_messages(entity, limit=100)
        
        for msg in messages:
            tags_in_msg = set(re.findall(r'#\w+', msg.text))
            
            if INTERESTING_TAGS & tags_in_msg:
                cursor.execute(
                    "INSERT OR IGNORE INTO posts(post_url, chat_id, hashtags) VALUES(?, ?, ?)",
                    (msg.link, entity.id, ', '.join(tags_in_msg))
                )
                
    conn.commit()

with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
    parse_groups(client)
