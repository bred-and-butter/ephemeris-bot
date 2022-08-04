from datetime import datetime

from discord_client import bot
from date_info.provider import provide_today_info


@bot.command(name="healthcheck")
async def health_check(ctx):
    await ctx.send("Bot ativo")


@bot.command(name="dayinfo")
async def day_info(ctx):
    await ctx.send(f"A informação do momento é: {datetime.now()}\n{provide_today_info()}")


@bot.command(name="exit")
async def shutdown(ctx):
    await ctx.send("Ephemeris-bot desligando...")
    exit()

