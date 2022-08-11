from discord.ext.commands import Bot

from bot_instance.cogs import BasicCog, JobCog
from jobs.manager import JobManager
from consts import PREFIX

bot = Bot(command_prefix=PREFIX)
job_handler = JobManager()


@bot.event
async def on_ready():
    print(f"{bot.user} active")
    bot.add_cog(BasicCog(bot))
    bot.add_cog(JobCog(bot=bot, job_handler=job_handler))
