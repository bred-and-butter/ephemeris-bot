from datetime import datetime

from discord.ext import tasks
import schedule

from bot_instance import bot
from date_info.provider import provide_today_info
from jobs import create_jobs


@bot.event
async def on_ready():
    create_jobs()
    job_check.start()
    print(f"{bot.user} active")


@tasks.loop(seconds=3)
async def job_check():
    print("checking for pending jobs...")
    schedule.run_pending()


@bot.command(name="ok?")
async def health_check(ctx):
    await ctx.send("ok 👍")


@bot.command(name="dayinfo")
async def day_info(ctx):
    await ctx.send(
        f"A data e hora atuais são: {datetime.now()}\n{provide_today_info()}"
    )


@bot.command(name="exit")
async def shutdown(ctx):
    await ctx.send("Ephemeris-bot desligando...")
    await bot.close()
