# src/parsers.py
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

async def parse_groups(client):
    participants = await client(GetParticipantsRequest(channel='@test_group', q='', offset=0, filter=ChannelParticipantsSearch(''), hash=0))
    for participant in participants.users:
        print(participant.username)
