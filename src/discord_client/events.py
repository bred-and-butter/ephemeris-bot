from discord_client import bot


@bot.event
async def on_ready():
    print(f"{bot.user} connected")

