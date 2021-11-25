import discord

from utils.greeting import welcome_message
from config import *
from utils.invites import generate_invites
from utils.helper import helper_command

class DenoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True

        super().__init__(intents=intents)
        self.__version__ = discord.__version__
        self.name = BOT_NAME

    async def on_member_join(self,member):
        channel = self.get_channel(WELCOME_CHANNEL)
        await channel.send(welcome_message(member.display_name))

    async def on_message(self,message):
        content = message.content
        if content.startswith("!deno"):
            channel = message.channel
            content = content.lstrip("!deno ").split(' ')
            if(content[0] == "commands" or content[0] == "help"): await helper_command(channel)
            elif(content[0] == "invites"): await generate_invites(self,channel)

    # async def on_member_remove(self,member):
    #     await member.send("oops")
    #     print(f"{member.display_name} left")

bot = DenoBot()
bot.run(BOT_TOKEN)