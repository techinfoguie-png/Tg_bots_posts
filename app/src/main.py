# src/main.py
from telethon.sync import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH
from handlers import handle_new_message
from parsers import parse_groups

async def main():
    client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    await client.start()
    await parse_groups(client)
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
"""
#or src/main.py
from telethon.sync import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, BOT_TOKEN
from handlers import handle_new_message
from parsers import parse_groups

client = TelegramClient('session_name', TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def main():
    await client.start(BOT_TOKEN)
    await parse_groups(client)
    await client.run_until_disconnected()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
"""
