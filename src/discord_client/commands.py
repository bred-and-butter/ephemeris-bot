from datetime import datetime

from discord_client import bot


@bot.command(name="dayinfo")
async def day_info(ctx):
    await ctx.send(f"A informação do momento é: {datetime.now()}")


@bot.command(name="exit")
async def shutdown(ctx):
    await ctx.send("Ephemeris-bot desligando...")
    exit()

