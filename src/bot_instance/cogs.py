from datetime import datetime

from discord.ext import tasks, commands

from date_info.provider import provide_date_info
from jobs import JobInterface
from consts import CHANNEL_ID, JOB_CHECK_PERIOD


class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ok?")
    async def health_check(self, ctx):
        await ctx.send("ok 👍")

    @commands.command(name="dayinfo")
    async def day_info(self, ctx):
        await ctx.send(f"{provide_date_info(year=0, month=0, day=0)}")

    @commands.command(name="exit")
    async def shutdown(self, ctx):
        await ctx.send("Ephemeris-bot desligando...")
        await self.bot.close()


class JobCog(commands.Cog):
    def __init__(self, bot: commands.Bot, job_handler: JobInterface) -> None:
        self.bot = bot
        self.job_handler = job_handler
        self.job_handler.init_jobs(self.write_to_chat)
        self.job_check.start()

    def write_to_chat(self):
        channel = self.bot.get_channel(int(CHANNEL_ID))
        message = provide_date_info(year=0, month=0, day=0)
        if channel:
            self.bot.dispatch("send_day_info", channel, message)
        else:
            print("error getting channel")

    @commands.Cog.listener(name="on_send_day_info")
    async def send_day_info(self, channel, message):
        await channel.send(message)

    @commands.command(name="startjob")
    async def start_job(self, ctx):
        try:
            self.job_check.start()
            await ctx.send("Tarefa iniciada")
        except RuntimeError:
            await ctx.send("Erro, tarefa já está rodando")

    @commands.command(name="stopjob")
    async def stop_job(self, ctx):
        self.job_check.stop()
        await ctx.send("Tarefa parada")

    @tasks.loop(seconds=int(JOB_CHECK_PERIOD))
    async def job_check(self):
        self.job_handler.job_check()
