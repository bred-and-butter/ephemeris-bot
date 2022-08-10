from datetime import datetime

from discord.ext import commands

from date_info.provider import provide_date_info


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ok?")
    async def health_check(self, ctx):
        await ctx.send("ok 👍")

    @commands.command(name="dayinfo")
    async def day_info(self, ctx):
        await ctx.send(
            f"A data e hora atuais são: {datetime.now()}\n{provide_date_info(year=0, month=0, day=0)}"
        )

    @commands.command(name="exit")
    async def shutdown(self, ctx):
        await ctx.send("Ephemeris-bot desligando...")
        await self.bot.close()
