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
"""
# Импортируем библиотеки
from telegram import Bot
from telegram.ext import Updater, CommandHandler
import logging

# Логгирование ошибок
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Токен вашего бота (полученный от BotFather)
TOKEN = 'ВАШ_ТОКЕН'

# Создаем объект бота
bot = Bot(TOKEN)

# Описание функций
def start(update, context):
    update.message.reply_text("Добро пожаловать в рассылку!")

def send_message_to_group(context):
    group_chat_id = '-ВАША_ID_ГРУППЫ'  # ID вашей группы в Telegram
    message = "Привет, группа!"
    context.bot.send_message(chat_id=group_chat_id, text=message)

# Основная логика бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Регистрация обработчика команды "/start"
    dp.add_handler(CommandHandler("start", start))
    
    # Планировщик заданий для ежедневной рассылки
    from datetime import time
    job_queue = updater.job_queue
    job_queue.run_daily(send_message_to_group, time(hour=10), days=(0, 1, 2, 3, 4, 5, 6))

    # Стартуем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    """
