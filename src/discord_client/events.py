from discord_client import client

@client.event
async def on_ready():
    print(f"{client.user} connected")
