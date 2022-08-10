from discord.ext.commands import Bot

from bot_instance.cogs import BasicCog
from jobs import JobCog
from consts import PREFIX

bot = Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print(f"{bot.user} active")
    bot.add_cog(BasicCog(bot))
    bot.add_cog(JobCog(bot))


