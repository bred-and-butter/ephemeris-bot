from discord.ext.commands import Bot
from consts import PREFIX

bot = Bot(command_prefix=PREFIX)


from .commands import *
