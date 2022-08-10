import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_NAME = os.getenv("GUILD_NAME")
CHANNEL_ID = os.getenv("CHANNEL_ID")
PREFIX = "%"
