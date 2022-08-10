import schedule
from discord.ext import tasks, commands

from date_info.provider import provide_date_info
from consts import CHANNEL_ID, JOB_CHECK_PERIOD, EPHEMERIS_FETCH_TIME


class JobCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        #schedule.every().day.at(EPHEMERIS_FETCH_TIME).do(self.write_to_chat)
        schedule.every(int(EPHEMERIS_FETCH_TIME)).seconds.do(self.write_to_chat)
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

    @tasks.loop(seconds=int(JOB_CHECK_PERIOD))
    async def job_check(self):
        print("checking for pending jobs...")
        schedule.run_pending()
