from discord.ext.commands import Bot
from consts import PREFIX

bot = Bot(command_prefix=PREFIX)


from .events import on_ready
from .commands import *
