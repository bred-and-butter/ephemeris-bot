from bot_instance import bot


@bot.event
async def on_ready():
    print(f"{bot.user} active")


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content == "oi":
#         response = "eai"
#         await message.channel.send(response)
#     else:
#         await message.channel.send(f"Você disse: {message.content}")
