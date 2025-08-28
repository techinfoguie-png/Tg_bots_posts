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
"""
# or src/handlers.py
from telethon.events import NewMessage
from utils.recommendations import predict_rating

async def handle_new_message(event):
    user_id = event.sender_id
    post_id = event.chat_id
    rating = predict_rating(user_id, post_id)
    print(f"Rating for user {user_id}, post {post_id}: {rating}")

async def register_handlers(client):
    client.add_event_handler(handle_new_message, NewMessage())
"""
