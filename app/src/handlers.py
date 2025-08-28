# src/handlers.py
from telethon.events import NewMessage
from utils.content_generator import generate_content
from utils.ml import generate_recommendation

async def handle_new_message(event):
    user_id = event.sender_id
    command = event.text.strip()

    if command.startswith('/generate'):
        _, topic = command.split(' ', maxsplit=1)
        generated_content = generate_content(topic)
        await event.respond(generated_content)
    elif command.startswith('/recommend'):
        _, content = command.split(' ', maxsplit=1)
        recommendation = generate_recommendation(user_id, content)
        await event.respond(recommendation)
