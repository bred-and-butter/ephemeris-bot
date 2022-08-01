import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_NAME = os.getenv('GUILD_NAME')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} connected")

client.run(TOKEN)